from app.views.clients import ClientViewSet
from app.views.orders import OrderViewSet
from app.views.produits import ProduitViewSet
from app.views.users import UserViewSet
from app.views.categories import CategorieViewSet

__all__ = [
    "CategorieViewSet",
    "ClientViewSet",
    "OrderViewSet",
    "ProduitViewSet",
    "UserViewSet",
]

