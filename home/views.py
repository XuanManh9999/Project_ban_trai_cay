from django.shortcuts import render
from django.http import HttpResponse
from .models import NguoiDung
from django.shortcuts import render, redirect
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
       # kiem tra xem email va password co ton tai trong bang nguoi dung khong
       user = NguoiDung.objects.filter(email=email, mat_khau=password).first()
       if user is not None:
            # luu thong tin nguoi dung vao session
            request.session['ID'] = user.id
            request.session['ho_va_ten'] = user.ho_va_ten
            request.session['email'] = user.email
            request.session['vai_tro'] = user.vai_tro
            #check role
            if user.vai_tro == 'admin':
                return redirect('manage-app')
            else:
                return redirect('home')
       else:
            messages.warning(request, 'Email hoặc mật khẩu không đúng!')
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
    # kiem tra xem nguoi dung co dang nhap chua va co phai la admin khong
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    context = {}
    return render(request, 'manage_app/base.html')
def manage_user(request):
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    data = NguoiDung.objects.all() # lay tat ca du lieu trong bang nguoi dung
    context = {
        'data': data
    }
    return render(request, 'manage_app/manage_user.html', context)
def manage_product(request):
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    context = {}
    return render(request, 'manage_app/manage_product.html')
def manage_order(request):
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    context = {}
    return render(request, 'manage_app/manage_order.html')
def manage_report(request):
    
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    context = {}
    return render(request, 'manage_app/manage_report.html')
def logout(request):
    # xoa session
    request.session.flush()
    return redirect('login')

    


    
    
    