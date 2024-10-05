from django.db import models

# Create your models here.

class NewsletterContact(models.Model):
    email = models.CharField(default="", null=False, blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Devis_client(models.Model):
    email = models.CharField(null=False, blank=False,max_length=255)
    telephone = models.CharField(null=False, blank=False,max_length=255)
    noms_prenoms = models.CharField(null=True, blank=True, max_length=255)
    article = models.CharField(null=True, blank=True,max_length=255)
    quantite = models.CharField(null=True, blank=True,max_length=255)
    designation = models.CharField(null=True, blank=True,max_length=255)
    dimensions = models.CharField(null=True, blank=True,max_length=255)
    created_at = created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Suggestion(models.Model):
    email = models.CharField(null=False, blank=False, max_length=255)
    nom_complet = models.CharField(null=False, blank=False, max_length=255)
    objet = models.CharField(null=True, blank=True,max_length=255)
    message = models.CharField(null=True, blank=True,max_length=255)