# Generated by Django 3.2.7 on 2021-10-04 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Edinet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Client', models.CharField(max_length=10)),
                ('Raison_sociale', models.CharField(max_length=255)),
                ('Commercial', models.CharField(max_length=100)),
                ('Adresse1', models.CharField(max_length=255)),
                ('Adresse2', models.CharField(max_length=255)),
                ('Code_postale', models.CharField(max_length=10)),
                ('Ville', models.CharField(max_length=255)),
                ('Pays', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Person',
            new_name='Utilisateur',
        ),
        migrations.CreateModel(
            name='Prestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Prestation', models.CharField(max_length=10)),
                ('Application', models.CharField(max_length=255)),
                ('PPNB', models.IntegerField()),
                ('APNB', models.IntegerField()),
                ('PPCL', models.IntegerField()),
                ('APCL', models.IntegerField()),
                ('LIASSE', models.IntegerField()),
                ('ARCHIV_AR', models.IntegerField()),
                ('P_LRE', models.IntegerField()),
                ('P_AVIS', models.IntegerField()),
                ('ID_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Edinet.client')),
            ],
        ),
        migrations.CreateModel(
            name='Info_client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Info', models.CharField(max_length=10)),
                ('Reglement', models.CharField(max_length=255)),
                ('Envoi_facture', models.DateField()),
                ('Type_Client', models.CharField(max_length=255)),
                ('Date_signature_contrat', models.DateField()),
                ('ID_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Edinet.client')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Contact', models.CharField(max_length=10)),
                ('Civilite', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=255)),
                ('Nom', models.CharField(max_length=255)),
                ('Fixe', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=255)),
                ('Adresse1', models.CharField(max_length=255)),
                ('Adresse2', models.CharField(max_length=255)),
                ('Code_postale', models.CharField(max_length=10)),
                ('Ville', models.CharField(max_length=255)),
                ('Pays', models.CharField(max_length=255)),
                ('Contact_facturation', models.BooleanField()),
                ('Fonction', models.CharField(max_length=255)),
                ('ID_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Edinet.client')),
            ],
        ),
    ]
