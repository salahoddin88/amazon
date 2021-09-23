from django.shortcuts import render, redirect
from product import models as ProductModels
from django.contrib.auth import authenticate, login
from django.contrib import messages
""" User Models """
from django.contrib.auth.models import User

def customerLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        """ Authenticate method will perfrom a match with submitted data and database """
        user = authenticate(request, username=username, password=password)
        if user is not None:
            """ Login method make user authorized """
            login(request, user)
            """ redirect will take url pattern name """
            return redirect('homePage')
        else:
            """ User can see this messages with defined tages in setting.py file """
            messages.error(request, 'Invlid Crendtials')
            return redirect('customerLogin')
    else:
        navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
        return render(request, 'customer-login.html', {
            'navigationProductCategories' : navigationProductCategories,
        })


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


def CategoryProducts(request, product_category_id):
    """ Products list according to category """
    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    products = ProductModels.Product.objects.filter(product_category_id=product_category_id)
    productCategories = ProductModels.ProductCategory.objects.filter(status=True)
    return render(request, 'category-products.html', {
        'navigationProductCategories' : navigationProductCategories,
        'products' : products,
        'productCategories':productCategories
    })

def ProductDetails(request, product_id):
    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    try:
        product = ProductModels.Product.objects.get(id=product_id)
    except ProductModels.Product.DoesNotExist:
        product= {}
    return render(request, 'product-details.html', {
        'navigationProductCategories' : navigationProductCategories,
        'product' :product
    })

def AddToCart(request, product_id):
    pass