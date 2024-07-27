from django.shortcuts import render, HttpResponse

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

def send_email_view(request):

    if request.method == 'POST':

        subject = f"Mensagem de: {request.POST.get('name')}"
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['christianoliveira8@outlook.com']
        data = {'name': name, 'email': email, 'message': message}
        message_body = get_template('homepage/send.html').render(data)
        print(message_body)

        print(type(settings.EMAIL_PORT))
        print(type(settings.EMAIL_USE_TLS))
        print(type(settings.EMAIL_TIMEOUT))
        print(settings.EMAIL_PORT)
        print(settings.EMAIL_USE_TLS)
        print(settings.EMAIL_TIMEOUT)
        try:
            send_mail(subject, message_body, from_email, recipient_list, fail_silently=False)
            return render(request, 'homepage/contact.html')
        except Exception as e:
            return HttpResponse(f'Error: {e}', status=500)
        
    return render(request, 'homepage/contact.html') 

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

# def send_email_view(request):

#     if request.method == 'POST':
        
#         email = {
#             'name': request.POST.get('name'),
#             'email': request.POST.get('email'),
#             'subject': f'Mensagem de {request.POST.get("name")}',
#             'message': request.POST.get('message')
#         }

#         try:
#             send_contact_email(email)
#             return render(request, 'homepage/contact.html')
#         except Exception as e:
#             HttpResponse(f'Error: {e}', status=500)

#     return render(request, 'homepage/contact.html')