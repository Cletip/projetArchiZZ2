from django.db import models

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    score = models.IntegerField()