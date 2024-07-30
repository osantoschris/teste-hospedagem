from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    payment = models.CharField(max_length=40)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
    def short_description(self):
        return self.description[:50] + '...' if len(self.description) > 50 else self.description
    
class FAQ(models.Model):
    product = models.ForeignKey(Product, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self) -> str:
        return f"FAQ for {self.product.name}: {self.question}"