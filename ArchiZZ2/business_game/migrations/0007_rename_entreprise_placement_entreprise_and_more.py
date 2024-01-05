# Generated by Django 4.2.6 on 2024-01-04 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_game', '0006_joueur_fond_disponible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placement',
            old_name='Entreprise',
            new_name='entreprise',
        ),
        migrations.AddField(
            model_name='entreprise',
            name='valeurBourse',
            field=models.FloatField(default=10.0),
        ),
        migrations.AlterUniqueTogether(
            name='placement',
            unique_together={('joueur', 'entreprise')},
        ),
        migrations.CreateModel(
            name='CoursBoursier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unite_temps', models.PositiveIntegerField()),
                ('valeur_bourse', models.FloatField(default=0.0)),
                ('entreprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_game.entreprise')),
            ],
            options={
                'unique_together': {('entreprise', 'unite_temps')},
            },
        ),
    ]
