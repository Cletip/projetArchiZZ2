# Generated by Django 4.2.6 on 2023-11-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_game', '0003_placement_argent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placement',
            old_name='idEntreprise',
            new_name='Entreprise',
        ),
        migrations.RenameField(
            model_name='placement',
            old_name='idjoueur',
            new_name='joueur',
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='cote',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='joueur',
            name='capital',
            field=models.FloatField(default=0.0),
        ),
    ]