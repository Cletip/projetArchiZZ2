# Generated by Django 4.2.6 on 2023-11-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='nom',
            field=models.CharField(default='Cacaprout&co', max_length=100),
        ),
        migrations.AddField(
            model_name='joueur',
            name='nom',
            field=models.CharField(default='Cacaprout', max_length=100),
        ),
    ]
