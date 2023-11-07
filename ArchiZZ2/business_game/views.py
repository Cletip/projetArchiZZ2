from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return HttpResponse("Bienvenue sur ma page d'accueil.")

def ma_vue_template(request):
    return render(request, 'template1.html')