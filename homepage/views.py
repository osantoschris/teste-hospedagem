from django.shortcuts import render

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