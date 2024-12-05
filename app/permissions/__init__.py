from app.permissions.clients import ClientsPermission
from app.permissions.orders import OrdersPermission
from app.permissions.produits import ProduitsPermission
from app.permissions.users import UsersPermission
from app.permissions.categories import CategoriesPermission

__all__ = [
    "CategoriesPermission",
    "ClientsPermission",
    "OrdersPermission",
    "ProduitsPermission",
    "UsersPermission"
]

