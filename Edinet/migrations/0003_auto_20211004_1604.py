# Generated by Django 3.2.7 on 2021-10-04 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Edinet', '0002_auto_20211004_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='birth_date',
            new_name='Date_de_naissance',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='phone_number',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='first_name',
            new_name='Nom',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='last_name',
            new_name='Prenom',
        ),
    ]
