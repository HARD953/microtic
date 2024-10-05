from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('galerie', views.gallery, name='galerie'),
    path('devis', views.devis, name='devis'),
    path('contact', views.contact, name='contact'),
]
