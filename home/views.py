from django.shortcuts import render
from django.http import HttpResponse
from .models import NguoiDung
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from home import 
# Create your views here.
def home(request):
    # tra ve template 
    return render(request, 'app/content.html')

def auth(request):
    context = {}
    return render(request, 'auth/base.html')
def content(request):
    context = {}
    return render(request, 'app/content.html')
def login(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       password = request.POST.get('password')  
       print(email, password)
    
    return render(request, 'auth/login.html')
def register(request):
    context = {}
    return render(request, 'auth/register.html')
def forgot_password(request):
    context = {}
    return render(request, 'auth/forgot-password.html')
def cart(request):
    context = {}
    return render(request, 'app/cart.html')
def checkout(request):
    context = {}
    return render(request, 'app/checkout.html')
def contact(request):
    context = {}
    return render(request, 'app/contact.html')
def shop(request):
    context = {}
    return render(request, 'app/shop.html')
def shop_details(request):
    context = {}
    return render(request, 'app/shop_detail.html')
def home_admin(request):
    context = {}
    return render(request, 'manage_app/base.html')
def manage_user(request):
    data = NguoiDung.objects.all() # lay tat ca du lieu trong bang nguoi dung
    context = {
        'data': data
    }
    return render(request, 'manage_app/manage_user.html', context)
def manage_product(request):
    context = {}
    return render(request, 'manage_app/manage_product.html')
def manage_order(request):
    context = {}
    return render(request, 'manage_app/manage_order.html')
def manage_report(request):
    context = {}
    return render(request, 'manage_app/manage_report.html')

    


    
    
    