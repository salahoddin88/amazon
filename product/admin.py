from django.contrib import admin

from . models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

admin.site.register(ProductCategory, ProductCategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_category', 'price', 'status']

admin.site.register(Product, ProductAdmin)