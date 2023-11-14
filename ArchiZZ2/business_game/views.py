from django.shortcuts import render
from django.http import HttpResponse
from .models import Joueur, Entreprise, Placement

def index(request):
    return render(request, 'index.html')

def simulation(request):
    return render(request, 'simulation.html')


def initialize_database(request):

    # Effacer tous les enregistrements existants
    Joueur.objects.all().delete()
    Entreprise.objects.all().delete()

    # Créer des joueurs
    joueur1 = Joueur.objects.create(capital=1000.0)
    joueur2 = Joueur.objects.create(capital=1500.0)

    # Créer des entreprises
    entreprise1 = Entreprise.objects.create(cote=50.0)
    entreprise2 = Entreprise.objects.create(cote=75.0)

    # Créer des placements
    placement1 = Placement.objects.create(idjoueur=joueur1, idEntreprise=entreprise1)
    placement2 = Placement.objects.create(idjoueur=joueur2, idEntreprise=entreprise2)

    return render(request, 'home.html')

def display_data(request):
    joueurs = Joueur.objects.all()
    entreprises = Entreprise.objects.all()
    placements = Placement.objects.all()

    context = {
        'joueurs': joueurs,
        'entreprises': entreprises,
        'placements': placements,
    }

    return render(request, 'home.html', context)
