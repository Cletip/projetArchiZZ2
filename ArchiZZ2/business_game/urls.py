from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulation/', views.simulation, name='simulation'),
    path('display_data/', views.display_data, name='display_data'),
    path('creer-nouveau-joueur/', views.creer_nouveau_joueur, name='creer_nouveau_joueur'),
    path('home/', views.home, name='home'),

]
