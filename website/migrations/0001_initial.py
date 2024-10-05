# Generated by Django 5.0.6 on 2024-06-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devis_client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField()),
                ('noms_prenoms', models.CharField(blank=True, null=True)),
                ('article', models.CharField(blank=True, null=True)),
                ('quantite', models.CharField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, null=True)),
                ('dimensions', models.CharField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='newsletterContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]