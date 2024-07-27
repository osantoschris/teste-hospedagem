from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products-services/', views.products, name='products-services'),
    # path('contact/', views.send_email, name='contact'),
    path('contact/', views.send_email_view, name='contact'),
    path('clients/', views.clients, name='clients'),
]
