# Generated by Django 4.2.6 on 2024-01-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_game', '0005_entreprise_description_entreprise_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='joueur',
            name='fond_disponible',
            field=models.FloatField(default=0.0),
        ),
    ]
