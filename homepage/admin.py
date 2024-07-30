from django.contrib import admin

# Register your models here.
from homepage import models

admin.site.register(models.Product)
admin.site.register(models.FAQ)