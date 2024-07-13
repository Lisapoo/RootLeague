# Generated by Django 5.0.6 on 2024-07-13 13:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0017_alter_match_board_map_alter_match_closed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='closed_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date closed'),
        ),
        migrations.AlterField(
            model_name='match',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date registered'),
        ),
    ]
