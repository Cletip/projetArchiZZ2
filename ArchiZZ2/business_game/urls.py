from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulation/', views.simulation, name='simulation'),
    path('initialize_database/', views.initialize_database, name='initialize_database'),
    path('display_data/', views.display_data, name='display_data'),
]
