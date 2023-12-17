from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NouveauJoueurForm
from .models import *

def index(request):
    return render(request, 'index.html')

def simulation(request):
    # Trouve le joueur avec l'ID le plus petit
    joueur_avec_petit_id = Joueur.objects.order_by('idjoueur').first()


    # suppression d'abord
    for entreprise in Entreprise.objects.all():
    #     # Récupérer la quantité d'argent investi pour cette entreprise
        supprimer_placement = request.POST.get(f'placement_{entreprise.idEntreprise}')
        if supprimer_placement == "supprime":
            # récupération argent placé
            placement = Placement.objects.filter(joueur=joueur_avec_petit_id, Entreprise=entreprise).first()
            joueur_avec_petit_id.capital += placement.argent
            joueur_avec_petit_id.save()

            # Supprimer tous les placements correspondants pour ce joueur et cette entreprise
            Placement.objects.filter(joueur=joueur_avec_petit_id, Entreprise=entreprise).delete()

    # Traitement des investissements
    for entreprise in Entreprise.objects.all():
    #     # Récupérer la quantité d'argent investi pour cette entreprise
        argent_investi = float(request.POST.get(f'E_{entreprise.idEntreprise}', 0))

        if argent_investi != 0:

            # Vérifie si un placement existe déjà pour ce joueur et cette entreprise
            placement_existant = Placement.objects.filter(joueur=joueur_avec_petit_id, Entreprise=entreprise).first()

            if placement_existant:
                # Si un placement existe, mettez à jour le montant
                placement_existant.argent += argent_investi
                placement_existant.save()
            else:
                # Sinon, créez un nouveau placement
                Placement.objects.create(
                    joueur=joueur_avec_petit_id,
                    Entreprise=entreprise,
                    argent=argent_investi
                )


        # Mettre à jour le capital du joueur
        joueur_avec_petit_id.capital -= argent_investi
        joueur_avec_petit_id.save()

    # Rediriger vers la page d'accueil après le traitement
    return redirect('home')

def initialize_database(NomJoueur, CapitalDep):

    # Effacer tous les enregistrements existants
    Joueur.objects.all().delete()
    Entreprise.objects.all().delete()

    # Création du joueur
    addJoueur(NomJoueur, CapitalDep)

    # Créer des bots
    bot1 = Joueur.objects.create(capital=1000.0, nom="Elon")
    bot2 = Joueur.objects.create(capital=1500.0, nom="Bezooos")

    # Créer des entreprises
    entreprise1 = Entreprise.objects.create(cote=50.0, nom="cacaland")
    entreprise2 = Entreprise.objects.create(cote=75.0, nom="pipiboudin")

    # Créer des placements
    placement1 = Placement.objects.create(joueur=bot1, Entreprise=entreprise1)
    placement2 = Placement.objects.create(joueur=bot2, Entreprise=entreprise2)

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
        # Récupérer les données POST
        data = request.POST

        # Vous pouvez accéder aux valeurs spécifiques par clé
        NomJoueur = data.get('Name')
        CapitalDep = data.get('Capital')

        initialize_database(NomJoueur, CapitalDep)

        # Faites quelque chose avec les données, par exemple, renvoyer une réponse
        return redirect('home')
 else:
     # Si la requête n'est pas de type POST, vous pouvez renvoyer une réponse différente
     return HttpResponse('Cette vue nécessite une requête POST.')
# {'form': form}
    # return render(request, 'mon_template.html', {'form': form})

def addPlacement(Joueur, entreprise, argent):
    Placement.objects.create(joueur=bot1, Entreprise=entreprise1, argent=1)
    return 0

def votre_vue(request):
    joueur_min_id = Joueur.objects.order_by('idjoueur').first().idjoueur
    placements = Placement.objects.filter(joueur=joueur_min_id)

    context = {
        'placements': placements,
        'joueur_min_id': joueur_min_id,
    }

    return render(request, 'votre_template.html', context)

def home(request):
    joueurs = Joueur.objects.all().order_by('-capital')
    entreprises = Entreprise.objects.all()

    # Trouve le joueur avec l'ID le plus petit
    joueur_avec_petit_id = Joueur.objects.order_by('idjoueur').first()
    placements = Placement.objects.filter(joueur=joueur_avec_petit_id)

    context = {
        'player' : joueur_avec_petit_id,
        'joueurs': joueurs,
        'entreprises': entreprises,
        'placements': placements,
    }

    if request.method == 'POST':
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)
