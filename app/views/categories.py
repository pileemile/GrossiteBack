from rest_framework.viewsets import ModelViewSet
from app.serializers.categories import CategorieSerializer
from app.models.categories import Categorie

class CategorieViewSet(ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer