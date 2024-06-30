# Generated by Django 3.0.3 on 2021-11-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='faction',
            field=models.CharField(blank=True, choices=[('cats', 'cats'), ('birds', 'birds'), ('alliance', 'alliance'), ('vagabond', 'vagabond')], max_length=100, null=True),
        ),
    ]
