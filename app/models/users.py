from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Supprimer is_superuser si non utilisé
    is_superuser = None

    # Définir des related_name uniques pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Nouveau nom unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Nouveau nom unique
        blank=True
    )
