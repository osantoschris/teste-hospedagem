from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

def send_contact_email(data):
    message_body = get_template('homepage/send.html').render(data)
    email = EmailMessage(data['subject'], 
                         message_body,
                         settings.DEFAULT_FROM_EMAIL, 
                         to=['christianoliveira8@outlook.com'])
    email.content_subtype = 'html'
    return email.send()

def send_email_view(request):

    if request.method == 'POST':

        subject = f"Mensagem de: {request.POST.get('name')}"
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['christianoliveira8@outlook.com']
        data = {
            'name': name, 
            'email': email, 
            'message': message, 
            'subject': subject
        }
        message_body = render_to_string('homepage/send.html', data)

        try:
            send_mail(
                subject=subject,
                message='', 
                from_email=from_email, 
                recipient_list=recipient_list, 
                fail_silently=False,
                html_message=message_body
            )

            return render(request, 'homepage/contact.html')
        except Exception as e:
            return HttpResponse(f'Error: {e}', status=500)
        
    return render(request, 'homepage/contact.html') 

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html', {})

def about(request):
    context = {
        'redirect_url': reverse('index')
    }
    return render(request, 'homepage/about.html', context)

def products(request):
    context = {
        'redirect_url': reverse('index')
    }
    return render(request, 'homepage/services.html', context)

def contact(request):
    return render(request, 'homepage/contact.html', {})

def clients(request):
    context = {
        'redirect_url': reverse('index')
    }
    return render(request, 'homepage/clients.html', context)