# Generated by Django 5.0.6 on 2024-08-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0032_alter_match_board_map_alter_match_deck_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='tournament_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='tournament score'),
        ),
    ]
