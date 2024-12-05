from django.db import models
from django.utils.timezone import now
from app.models.clients import Client
from app.models.produits import Produit
from app.models.users import User



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(default=now)
    quantite = models.IntegerField()
    statut = models.CharField(max_length=50, choices=[
        ('EN ATTENTE', 'En attente'),
        ('TRAITÉE', 'Traitée'),
    ])
