# Generated by Django 4.2.6 on 2023-11-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_game', '0002_entreprise_nom_joueur_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='argent',
            field=models.FloatField(default=0.0),
        ),
    ]
