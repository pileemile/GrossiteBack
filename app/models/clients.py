from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    siret = models.CharField(max_length=14)

    def __str__(self):
        return self.nom