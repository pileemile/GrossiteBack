from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'detail': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            # Générer le token JWT
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Sérialiser l'utilisateur pour l'ajouter à la réponse
            user_data = UserSerializer(user).data

            # Retourner le token et les informations de l'utilisateur
            return Response({
                'refresh': str(refresh),
                'access': access_token,
                'user': user_data
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
