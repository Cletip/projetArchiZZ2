# Generated by Django 4.2.6 on 2024-01-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_game', '0007_rename_entreprise_placement_entreprise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='event_impact',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='joueur',
            name='unite_temps',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
