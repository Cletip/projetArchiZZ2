from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse
from .forms import NouveauJoueurForm
from .models import *
from .constants import *
import random

def index(request):
    return render(request, 'index.html')

def simuler_evenement():
    # Tirage aléatoire entre 0 et 100
    tirage = random.randint(0, 100)


    # Renvoie d'un tuple avec en premier l'evenement et ensuite le pourcentage appliqué
    # Déterminer l'événement en fonction du tirage
    if tirage < 5:
        return (random.choice(EVENEMENTS_TRES_MAUVAIS), -0.7)
    elif tirage < 15:
        return (random.choice(EVENEMENTS_MAUVAIS), -0.3)
    elif tirage < 25:
        return (random.choice(EVENEMENTS_BON), 0.2)
    elif tirage < 30:
        return (random.choice(EVENEMENTS_TRES_BON), 0.4)
    else:
        return ('none', 0.0)  # Aucun événement ne s'est produit

def suppresion_placement(request, joueur):
    for entreprise in Entreprise.objects.all():
        # Récupérer la quantité d'argent investi pour cette entreprise
        supprimer_placement = request.POST.get(f'placement_{entreprise.idEntreprise}')
        if supprimer_placement == "supprime":
            # récupération argent placé
            placement = Placement.objects.filter(joueur=joueur, entreprise=entreprise).first()
            joueur.fond_disponible += round(placement.argent, 2)
            joueur.save()

            # Supprimer tous les placements correspondants pour ce joueur et cette entreprise
            Placement.objects.filter(joueur=joueur, entreprise=entreprise).delete()

def nouveau_investissement(request, joueur):
    for entreprise in Entreprise.objects.all():
        # Récupérer la quantité d'argent investi pour cette entreprise
        argent_investi = float(request.POST.get(f'E_{entreprise.idEntreprise}', 0))

        if argent_investi != 0:

            # Vérifie si un placement existe déjà pour ce joueur et cette entreprise
            placement_existant = Placement.objects.filter(joueur=joueur, entreprise=entreprise).first()

            if placement_existant:
                # Si un placement existe, mettez à jour le montant
                placement_existant.argent += argent_investi
                placement_existant.save()
            else:
                # Sinon, créez un nouveau placement
                Placement.objects.create(
                    joueur=joueur,
                    entreprise=entreprise,
                    argent=argent_investi
                )


        # Mettre à jour le capital du joueur
        joueur.fond_disponible -= argent_investi
        joueur.save()

def maj_entreprise(time):
    for entreprise in Entreprise.objects.all():
        # Générer un facteur aléatoire pour l'évolution des valeurs boursieres (par exemple, entre -35% et +35%)
        variation_percent = random.uniform(-0.35, 0.35)
        
        # Mettre à jour la cote de l'entreprise
        prev = entreprise.valeurBourse
        entreprise.valeurBourse *= (1 + variation_percent + entreprise.event_impact)
        entreprise.valeurBourse = round(entreprise.valeurBourse, 2)

        addCoursBoursier(entreprise, time)
        
        #calcule de la cote de l'entreprise en bourse en pourcentage
        entreprise.cote = round((entreprise.valeurBourse - prev)*100/prev, 2) 

        event = simuler_evenement()

        entreprise.event = event[0]
        entreprise.event_impact = event[1]

        entreprise.save()

def maj_placement():
    # Mise à jour des placements et des capitaux des joueurs
    for joueur in Joueur.objects.all():
        # Mettre à jour les placements du joueur en fonction des nouvelles cotes
        for placement in Placement.objects.filter(joueur=joueur):
            entreprise = placement.entreprise
            argent_investi = placement.argent
            variation_percent = entreprise.cote
            variation_amount = argent_investi * variation_percent / 100
            placement.argent = round(argent_investi + variation_amount, 2)
            placement.save()

            # Mettre à jour le capital du joueur en conséquence
            joueur.capital += placement.argent - argent_investi
            joueur.capital = round(joueur.capital, 2)  
            joueur.save()


def simulation(request):
    # Trouve le joueur avec l'ID le plus petit aka notre véritable joueur
    joueur_avec_petit_id = Joueur.objects.order_by('idjoueur').first()

    # Récupération et Incrémentation de l'unité de temps
    unite_temps = joueur_avec_petit_id.unite_temps
    unite_temps += 1

    # Mettre à jour la valeur de l'unité de temps dans la base de données
    joueur_avec_petit_id.unite_temps = unite_temps
    joueur_avec_petit_id.save()

    # suppression d'abord
    suppresion_placement(request, joueur_avec_petit_id)
    
    # Traitement des investissements
    nouveau_investissement(request, joueur_avec_petit_id)

    # Évolution aléatoire des valeurs des entreprises
    maj_entreprise(unite_temps)

    maj_placement()

    # Rediriger vers la page d'accueil après le traitement
    return redirect('home')

def initialize_database(NomJoueur, CapitalDep):

    # Effacer tous les enregistrements existants
    Joueur.objects.all().delete()
    Entreprise.objects.all().delete()

    # Création du joueur
    addJoueur(NomJoueur, CapitalDep)

    # Créer des bots
    bot1 = addJoueur("Elon", 1000.0)
    bot2 = addJoueur("Bezoos", 1500.0)
    bot3 = addJoueur("Boloré", 2000.0)
    bot4 = addJoueur("Mr.Beast", 1500.0)

    # Créez 4 instances d'entreprise avec des noms et des cotes diverses
    entreprise1 = addEntreprise("SeriousCorp", "SeriousCorp Solutions est bien plus qu'une simple entreprise. Nous sommes des pionniers dans le domaine de la fourniture de solutions professionnelles, mettant l'accent sur la rigueur, la fiabilité et l'efficacité. Notre engagement envers la satisfaction client et notre approche sérieuse font de nous le partenaire idéal pour résoudre vos défis professionnels les plus complexes. Avec SeriousCorp, chaque solution est conçue avec la plus grande attention aux détails, reflétant notre engagement envers l'excellence professionnelle.")
    entreprise2 = addEntreprise("ProInvest", "ProInvest Responsable est bien plus qu'une entreprise d'investissement. Nous sommes les gardiens d'un avenir durable, dédiés à l'investissement responsable et éthique. Chez ProInvest, nous croyons que les investissements peuvent avoir un impact positif sur la planète. Notre engagement envers la durabilité, la transparence et la responsabilité fait de nous le choix idéal pour ceux qui cherchent à investir non seulement pour le rendement financier, mais aussi pour un monde meilleur.")
    entreprise3 = addEntreprise("GlobalTech", "GlobalTech Innovations est à l'avant-garde de la révolution technologique, offrant des solutions mondiales qui transcendent les frontières. Nous sommes bien plus qu'une entreprise technologique standard - nous sommes les architectes du futur numérique. Notre engagement envers l'innovation, la créativité et la qualité fait de nous le leader incontesté dans la fourniture de solutions technologiques qui repoussent les limites. Chez GlobalTech, chaque innovation est une étape vers un avenir technologique plus intelligent et plus connecté.")
    entreprise4 = addEntreprise("InnoSolutions", "InnoSolutions Créatives n'est pas seulement une entreprise, c'est une force créatrice dédiée à résoudre les défis commerciaux actuels par le biais de l'innovation. Nous sommes les architectes de solutions novatrices, combinant créativité et expertise pour transformer les obstacles en opportunités. Chez InnoSolutions, chaque défi est une invitation à repousser les limites de la créativité et de l'ingéniosité pour trouver des solutions uniques qui façonnent l'avenir des affaires.")
    entreprise5 = addEntreprise("DataPulse", "DataPulse Solutions est une entreprise innovante spécialisée dans l'analyse et l'optimisation de données. Nous exploitons la puissance des pulsations de données pour offrir des solutions avancées d'analyse, de visualisation et de gestion des données à nos clients. Que ce soit pour découvrir des tendances cachées, améliorer l'efficacité opérationnelle ou prendre des décisions éclairées, DataPulse excelle dans l'extraction de la quintessence des données pour propulser nos clients vers l'avenir.")
    entreprise6 = addEntreprise("NanoVerse", "NanoVerse Technologies émerge comme une puissance dans le monde de la technologie, explorant l'infiniment petit pour créer des solutions exceptionnelles. Bien plus qu'une simple entreprise technologique, nous sommes les pionniers de l'infiniment petit, exploitant les nanotechnologies pour transformer la façon dont nous percevons et utilisons la technologie. Chez NanoVerse, chaque innovation est ancrée dans notre engagement envers la précision, l'efficacité et l'exploration des frontières de la science.")

    # ajouter les valeurs initiales des entreprises dans le cours boursier
    addCoursBoursier(entreprise1, 1)
    addCoursBoursier(entreprise2, 1)
    addCoursBoursier(entreprise3, 1)
    addCoursBoursier(entreprise4, 1)
    addCoursBoursier(entreprise5, 1)
    addCoursBoursier(entreprise6, 1)

    # Créer des placements
    addPlacement(bot1, entreprise1, 350)
    addPlacement(bot2, entreprise2, 250)
    addPlacement(bot3, entreprise3, 300)
    addPlacement(bot4, entreprise4, 270)


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


def home(request):
    joueurs = Joueur.objects.all().order_by('-capital')
    entreprises = Entreprise.objects.all()

    # Trouve le joueur avec l'ID le plus petit
    joueur_avec_petit_id = Joueur.objects.order_by('idjoueur').first()
    placements = Placement.objects.filter(joueur=joueur_avec_petit_id)

    # Récupérez les données CoursBoursier pour chaque entreprise
    cours_boursier_data = {}
    for entreprise in entreprises:
        cours_boursier_data[entreprise.idEntreprise] = serialize('json', CoursBoursier.objects.filter(entreprise=entreprise))

    context = {
        'player' : joueur_avec_petit_id,
        'joueurs': joueurs,
        'entreprises': entreprises,
        'placements': placements,
        'cours_boursier_data': cours_boursier_data,
    }

    if request.method == 'POST':
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)
