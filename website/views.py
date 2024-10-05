from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsletterContact, Devis_client, Suggestion

from django.contrib.auth.models import User

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# from django.core.mail import EmailMessage
from microtic.settings import EMAIL_HOST_USER

# Create your views here.
def newsletter(request, page):
    context = {}
    if request.method == "POST":
        _email = request.POST.get("email")
        try:
            subscriber = NewsletterContact.objects.get(email=_email)
            if subscriber is not None:
                context = {
                    "message": "Cette adresse mail existe déjà"
                }
        except NewsletterContact.DoesNotExist:
            NewsletterContact.objects.create(email=_email)
            context = {
                "message": "Le mail a bien été enregistré"
            }
    return context

def home(request):
    context = newsletter(request, 'pages/accueil.html')
    return render(request, 'pages/accueil.html', context)

def services(request):
    page = 'pages/services.html'
    context = newsletter(request, page)
    return render(request, page, context)

def gallery(request):
    page = 'pages/gallery.html'
    context = newsletter(request, page)
    return render(request, page, context)

def devis(request):
    page = 'pages/booking.html'
    if request.method == "POST":
        nom_complet = request.POST.get("nom_complet")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        article = request.POST.get("article")
        designation = request.POST.get("designation")
        quantite = request.POST.get("quantite")
        dimensions = request.POST.get("dimensions")

        Devis_client.objects.create(
            noms_prenoms=nom_complet,
            telephone=telephone,
            email=email,
            article=article,
            designation=designation,
            quantite=quantite,
            dimensions=dimensions
        )
        subject = "New Order is placed"
        my_recipient = email
        if User.objects.filter(email=my_recipient).exists():
            user = User.objects.get(email=my_recipient)
            nameUser = str(nom_complet)
            telephone = telephone
            email = email
            article = article
            designation = designation
            quantite = str(quantite)
            dimension = dimensions
        else :
            None
        link_app = "http://127.0.0.1:8000/"
        context = {
            "nameUser": nameUser,
            "telephone": telephone,
            "email" : email,
            "article": article,
            "designation": designation,
            "quantite": quantite,
            "dimension": dimension,
            "link_app": link_app
        }


        html_message = render_to_string("email/email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject= nom_complet,
            body= plain_message,
            from_email= None,
            to= [email]
        )
        message.attach_alternative(html_message, "text/html")
        message.send()



        # recipient_list = [email]
        # send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)
        
    return render(request, page)

def contact(request):
    page = 'pages/contact.html'
    if request.method == "POST":
        nom_complet = request.POST.get("nom_complet")
        email = request.POST.get("email")
        objet = request.POST.get("objet")
        message = request.POST.get("message")

        Suggestion.objects.create(
            nom_complet=nom_complet,
            email=email,
            objet=objet,
            message=message
        )
    return render(request, page)

def custom_page_not_found_view(request, exception):
    return render(request, 'pages/404.html', status=404)
