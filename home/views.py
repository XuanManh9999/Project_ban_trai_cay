from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from home.models import NguoiDung
def home(request):
    data = NguoiDung.objects.all()
    print(data)
    # tra ve template 
    return render(request, 'app/content.html', {'data': data})

def auth(request):
    context = {}
    return render(request, 'auth/base.html')
def content(request):
    context = {}
    return render(request, 'app/content.html')
def login(request):
    context = {}
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