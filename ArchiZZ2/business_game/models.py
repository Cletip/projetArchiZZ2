from django.db import models

class Joueur(models.Model):
    idjoueur = models.AutoField(primary_key=True)
    unite_temps = models.PositiveIntegerField(default=1)
    nom = models.CharField(max_length=100, default='Cacaprout')  # Ajout du champ "nom"
    capital = models.FloatField(default=0.0)
    fond_disponible = models.FloatField(default=0.0)

class Entreprise(models.Model):
    idEntreprise = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100,default='Cacaprout&co')  # Ajout du champ "nom"
    valeurBourse = models.FloatField(default=10.0)
    cote = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)  
    event = models.CharField(max_length=255, blank=True, null=True, default='none') 
    event_impact = models.FloatField(default=0.0)

class Placement(models.Model):
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    argent = models.FloatField(default=0.0)  # Champ float

    class Meta:
        # Définir la clé primaire composite
        unique_together = ('joueur', 'entreprise')

class CoursBoursier(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    unite_temps = models.PositiveIntegerField()  # Ajoutez la variable de temps
    valeur_bourse = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('entreprise', 'unite_temps')




def addJoueur(Name="NomJoueur", Capital=1500):
    return Joueur.objects.create(capital=Capital, fond_disponible=Capital, nom=Name)

def addPlacement(j, e, a):
    return Placement.objects.create(joueur = j, entreprise = e, argent = a)

def addEntreprise(Name="DefaultEntreprise", desc="description", value=10.0):
    return Entreprise.objects.create(nom=Name, description=desc, valeurBourse=value)

def addCoursBoursier(e, time):
    return CoursBoursier.objects.create(entreprise = e, unite_temps = time, valeur_bourse = e.valeurBourse)