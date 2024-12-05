from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from app.models.users import User
from app.serializers.users import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Vérifier si le nom d'utilisateur et le mot de passe sont fournis
        if not username or not password:
            return Response({'detail': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Récupérer l'utilisateur correspondant
        user = User.objects.filter(username=username).first()

        if user is not None:
            # Vérifier si le mot de passe correspond avec check_password
            if check_password(password, user.password):
                # Si les identifiants sont corrects, générer le token JWT
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # Sérialiser l'utilisateur pour l'ajouter à la réponse
                return Response({
                    'refresh': str(refresh),
                    'access': access_token,
                    'user': UserSerializer(user).data
                })
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
