# Generated by Django 5.1.1 on 2024-09-19 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaborador',
            old_name='mome',
            new_name='nome',
        ),
    ]
