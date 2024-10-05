# Generated by Django 5.0.6 on 2024-06-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_devis_client_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField()),
                ('nom_complet', models.CharField()),
                ('objet', models.CharField(blank=True, null=True)),
                ('message', models.CharField(blank=True, null=True)),
            ],
        ),
    ]
