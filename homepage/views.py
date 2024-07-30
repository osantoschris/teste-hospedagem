from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.detail import DetailView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

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

            return render(request, 'homepage/thanks_page.html')
        except Exception as e:
            return HttpResponse(f'Error: {e}', status=500)
        
    return render(request, 'homepage/contact.html') 

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html', {})

def about(request):
    return render(request, 'homepage/about.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'homepage/services.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'homepage/product_detail.html', {'product': product})

def clients(request):
    context = {
        'redirect_url': reverse('index')
    }
    return render(request, 'homepage/clients.html', context)