from rest_framework.viewsets import ModelViewSet
from app.models.orders import Order
from app.serializers.orders import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
