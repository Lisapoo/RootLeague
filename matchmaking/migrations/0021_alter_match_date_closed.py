# Generated by Django 5.0.6 on 2024-07-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0020_remove_match_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date_closed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date closed'),
        ),
    ]
