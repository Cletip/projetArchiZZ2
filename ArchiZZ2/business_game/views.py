from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NouveauJoueurForm
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
    joueur1 = Joueur.objects.create(capital=1000.0, nom="clement")
    joueur2 = Joueur.objects.create(capital=1500.0, nom="pierre le boss")

    # Créer des entreprises
    entreprise1 = Entreprise.objects.create(cote=50.0, nom="cacaland")
    entreprise2 = Entreprise.objects.create(cote=75.0, nom="pipiboudin")

    # Créer des placements
    placement1 = Placement.objects.create(idjoueur=joueur1, idEntreprise=entreprise1)
    placement2 = Placement.objects.create(idjoueur=joueur2, idEntreprise=entreprise2)

    return display_data(request)

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




def creer_nouveau_joueur(request):
    if request.method == 'POST':
        form = NouveauJoueurForm(request.POST)
        if form.is_valid():
            nom_joueur = form.cleaned_data['nom']

            # Crée un nouveau joueur dans la table des joueurs
            nouveau_joueur = Joueur.objects.create(nom=nom_joueur)

            # Redirige vers l'URL de simulation
            return redirect('simulation')
    else:
        form = NouveauJoueurForm()

    return display_data(request)