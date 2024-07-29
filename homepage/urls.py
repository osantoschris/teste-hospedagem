from django.urls import path
from . import views
from .views import ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products-services/', views.products, name='products-services'),
    path('contact/', views.send_email_view, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('products-services/<int:pk>', ProductDetailView.as_view(), name='products-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)