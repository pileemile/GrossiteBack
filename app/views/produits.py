from rest_framework.viewsets import ModelViewSet
from app.models.produits import  Produit
from app.serializers.produits import  ProduitSerializer

class ProduitViewSet(ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
