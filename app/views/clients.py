from app.serializers.clients import ClientSerializer
from rest_framework.viewsets import ModelViewSet
from app.models.orders import Client

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer