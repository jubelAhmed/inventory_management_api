from django.contrib import admin
from .models import Inventory,Supplier

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Inventory)
