from django.shortcuts import render
from product import models as ProductModels


def homePage(request):
    """ Home page Render Function """    

    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    productCategories = ProductModels.ProductCategory.objects.filter(status=True)
    products = ProductModels.Product.objects.filter(status=True).order_by('-id')[:3]

    return render(request, 'index.html', {
        'navigationProductCategories' : navigationProductCategories,
        'productCategories' : productCategories,
        'products' : products
    })

  