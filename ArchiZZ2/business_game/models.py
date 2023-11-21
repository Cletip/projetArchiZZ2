from django.db import models

class Joueur(models.Model):
    idjoueur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, default='Cacaprout')  # Ajout du champ "nom"
    capital = models.DecimalField(max_digits=10, decimal_places=2)

class Entreprise(models.Model):
    idEntreprise = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100,default='Cacaprout&co')  # Ajout du champ "nom"
    cote = models.DecimalField(max_digits=5, decimal_places=2)

class Placement(models.Model):
    idjoueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    idEntreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    argent = models.FloatField(default=0.0)  # Champ float


def addJoueur(Name="NomJoueur", Capital=1500):
    print(Name)
    return Joueur.objects.create(capital=Capital, nom=Name)
