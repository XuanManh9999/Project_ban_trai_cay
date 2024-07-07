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
    #admin
    path('manage-app/', views.home_admin, name="manage-app"),
    path('manage-user/', views.manage_user, name="manage-user"),
    path('manage-product/', views.manage_product, name="manage-product"),
    path('manage-order/', views.manage_order, name="manage-order"),
    path('manage-report/', views.manage_report, name="manage-report"),
    path('logout/', views.logout, name="logout")
    
    
]
