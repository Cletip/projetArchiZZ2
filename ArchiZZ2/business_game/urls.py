from django.urls import path
from . import views

urlpatterns = [
    path('template1/', views.ma_vue_template, name='template1'),
    path('', views.accueil, name='page_accueil'),
]