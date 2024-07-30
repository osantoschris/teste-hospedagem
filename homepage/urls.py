from django.urls import path
from . import views
from .views import ProductDetailView
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.send_email_view, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('products-services/', views.products, name='products-services'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
]