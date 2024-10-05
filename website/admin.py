from django.contrib import admin
from .models import Devis_client, NewsletterContact, Suggestion

# Register your models here.

class DevisAdmin(admin.ModelAdmin):
    list_display = ('id','noms_prenoms','article','designation','quantite','telephone','email', 'dimensions')
    list_filter = ('id','noms_prenoms','article','designation','quantite','telephone','email', 'dimensions')
    search_fields = ('id','noms_prenoms','article','designation','quantite','telephone','email', 'dimensions')

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('id','nom_complet','email','objet','message')
    list_filter = ('id','nom_complet','email','objet','message')
    search_fields = ('id','nom_complet','email','objet','message')

class NewsletterContactAdmin(admin.ModelAdmin):
    list_display = ('id','email',)
    list_filter = ('id','email',)
    search_fields = ('id','email',)

admin.site.register(Devis_client, DevisAdmin)
admin.site.register(NewsletterContact, NewsletterContactAdmin)
admin.site.register(Suggestion, SuggestionAdmin)