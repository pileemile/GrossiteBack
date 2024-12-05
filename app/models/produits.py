from django.db import models
from app.models.categories import Categorie


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    date_peremtion = models.DateTimeField(null=True, blank=True)
    emplacement = models.CharField(max_length=100)
