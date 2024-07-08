"""
URL configuration for Python_Web_Ban_Trai_Cay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import  views


urlpatterns = [
    path('', views.home, name="home"),
    path('auth/', views.auth, name="auth"),
    path('content/', views.content, name="content"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('shop-detail/', views.shop_details, name="shop_details"),
    path('cart-order/', views.cart_order, name="cart_order"),
    path('state-order/', views.state_order, name="state_order"),
    path('submid-order/<int:order_id>/', views.da_nhan_hang, name='da_nhan_hang'),
    #admin
    path('manage-app/', views.home_admin, name="manage-app"),
    path('manage-user/', views.manage_user, name="manage-user"),
    #delete user
    path('delete-user/<int:id>', views.delete_user, name="delete-user"),
    path('manage-product/', views.manage_product, name="manage-product"),
    #delete product
    path('delete-product/<int:id>', views.delete_product, name="delete-product"),
    path('manage-order/', views.manage_order, name="manage-order"),
    #detail-order
    path('detail-order/<int:order_id>/', views.detail_order, name='detail_order'),
    # confirm_order
    path('confirm-order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    # huy don hang
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    #cancel_order_user
    path('cancel-order-user/<int:order_id>/', views.cancel_order_user, name='cancel_order_user'),
    path('manage-report/', views.manage_report, name="manage-report"),
    path('manage-category/', views.manage_category, name="manage-category"),
    #delete category
    path('delete-category/<int:id>', views.delete_category, name="delete-category"),
    path('logout/', views.logout, name="logout"),
    #add_product_to_cart
    path('add-product-to-cart/<int:id>', views.add_product_to_cart, name="add-product-to-cart"),
    #minus_product_to_cart
    path('minus-product-to-cart/<int:id>', views.minus_product_to_cart, name="minus-product-to-cart"),
    #delete_product_to_cart
    path('delete-product-to-cart/<int:id>', views.delete_product_in_cart, name="delete-product-to-cart"),
    
    
]
