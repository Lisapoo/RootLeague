# Generated by Django 5.0.6 on 2024-07-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0010_alter_match_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='closed',
            field=models.BooleanField(db_default=True, default=True),
        ),
    ]
