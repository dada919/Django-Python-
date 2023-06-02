from django.db import models

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
