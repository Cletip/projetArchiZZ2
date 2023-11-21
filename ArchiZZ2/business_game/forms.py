from django import forms

class NouveauJoueurForm(forms.Form):
    nom = forms.CharField(label='Nom du joueur', max_length=100)