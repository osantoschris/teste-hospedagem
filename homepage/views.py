from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactMeForm

from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail

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

def send_email(request):
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            email = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'subject': f'Email de {request.POST.get("name")} - {request.POST.get("email")}',
                'message': request.POST.get('message'),
            }

            send_contact_email(email)
            return redirect('contact')
    else:
        form = ContactMeForm()

    return render(request, 'homepage/contact.html', {'form': form})