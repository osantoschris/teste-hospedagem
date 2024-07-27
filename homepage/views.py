from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactMeForm

from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage

def send_contact_email(data):
    message_body = get_template('homepage/send.html').render(data)
    email = EmailMessage(data['subject'], 
                         message_body,
                         settings.DEFAULT_FROM_EMAIL, 
                         to=['christianoliveira8@outlook.com'])
    email.content_subtype = 'html'
    return email.send()

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html', {})

def about(request):
    return render(request, 'homepage/about.html', {})

def products(request):
    return render(request, 'homepage/services.html', {})

def contact(request):
    return render(request, 'homepage/contact.html', {})

def clients(request):
    return render(request, 'homepage/clients.html', {})

def send_email_view(request):

    if request.method == 'POST':
        
        email = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'subject': f'Mensagem de {request.POST.get("name")}',
            'message': request.POST.get('message')
        }

        try:
            send_contact_email(email)
            return render(request, 'homepage/contact.html')
        except Exception as e:
            HttpResponse(f'Error: {e}', status=500)

    return render(request, 'homepage/contact.html')