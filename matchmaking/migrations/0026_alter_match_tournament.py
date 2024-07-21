# Generated by Django 5.0.6 on 2024-07-21 09:19

import django.db.models.deletion
import league.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
        ('matchmaking', '0025_match_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(default=league.models.Tournament.get_default_pk, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='league.tournament', verbose_name='tournament'),
        ),
    ]
