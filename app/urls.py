from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.views.login import LoginView
from app.views.users import UserViewSet
from app.views.produits import  ProduitViewSet
from app.views.orders import OrderViewSet
from app.views.categories import CategorieViewSet
from app.views.clients import ClientViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')
router.register('categories', CategorieViewSet, basename='categorie')
router.register('produits', ProduitViewSet, basename='produit')
router.register('clients', ClientViewSet, basename='client')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/auth/login/', LoginView.as_view(), name='login'),
]
urlpatterns += router.urls

