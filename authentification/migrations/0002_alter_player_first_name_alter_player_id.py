# Generated by Django 4.1 on 2024-06-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
