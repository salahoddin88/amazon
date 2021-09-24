from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('login', views.customerLogin, name="customerLogin"),
    path('logout', views.customerLogout, name="customerLogout"),
    path('registration', views.CustomerRegistration, name="CustomerRegistration"),
    path('category-product/<int:product_category_id>', views.CategoryProducts, name="CategoryProducts"),
    path('product-details/<int:product_id>', views.ProductDetails, name="ProductDetails"),
    path('add-to-cart/<int:product_id>', views.AddToCart, name="AddToCart"),
    path('cart', views.CustomerCart, name="CustomerCart"),
    path('delete-cart-product/<int:cart_id>', views.DeleteCartProduct, name="DeleteCartProduct"),
]
