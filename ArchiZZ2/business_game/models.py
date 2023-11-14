from django.db import models

class Joueur(models.Model):
    idjoueur = models.AutoField(primary_key=True)
    capital = models.DecimalField(max_digits=10, decimal_places=2)

class Entreprise(models.Model):
    idEntreprise = models.AutoField(primary_key=True)
    cote = models.DecimalField(max_digits=5, decimal_places=2)

class Placement(models.Model):
    idjoueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    idEntreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
