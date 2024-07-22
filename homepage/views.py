from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse

import smtplib
import email.message

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
        nome = request.POST.get("nome")
        mensagem = request.POST.get("msg")
        destinatario = request.POST.get("email")

        # Configuração do email
        email_msg = email.message.EmailMessage()
        email_msg['Subject'] = f'Email de {nome}'
        email_msg['From'] = settings.EMAIL_HOST_USER
        email_msg['To'] = destinatario
        email_msg.set_content(mensagem, subtype='html')

        # Conectar ao servidor SMTP
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(email_msg)
        except Exception as e:
            return HttpResponse(f'Erro ao enviar email: {e}')

        return HttpResponse('E-mail enviado com sucesso!')

    return render(request, 'homepage/contact.html')