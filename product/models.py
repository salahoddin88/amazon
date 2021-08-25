from django.db import models
from django.db.models.base import Model


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.name)


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField()
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.name)
    