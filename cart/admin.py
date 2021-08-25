from django.contrib import admin
from . models import Cart


class CartModel(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity']
    
admin.site.register(Cart, CartModel)

