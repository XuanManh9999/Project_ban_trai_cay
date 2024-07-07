from django.shortcuts import render
from django.http import HttpResponse
from .models import NguoiDung, SanPham, LoaiSanPham
from django.shortcuts import render, redirect
from django.contrib import messages
# from home import 
# Create your views here.
def home(request):
    #lay tat ca san pham
    all_products = SanPham.objects.all()
    #lay tat ca loai san pham
    all_categories = LoaiSanPham.objects.all()
    #fort mart all product tien 
    for product in all_products:
        product.gia_san_pham = "{:,.2f}".format(product.gia_san_pham)
    # dem so luong san pham trong gio hang
    total_quantity = 0
    list_cart = request.session.get('list_products_in_cart')
    if list_cart is not None:
        for item in list_cart:
            total_quantity = total_quantity + item['quantity']
        
    context = {
        'products': all_products,
        'categories': all_categories,
        'total_quantity': total_quantity
    }
    return render(request, 'app/content.html', context)

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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        sdt = request.POST.get('sdt')
        password = request.POST.get('password')
        # kiem tra xem email da ton tai trong bang nguoi dung chua
        user = NguoiDung.objects.filter(email=email).first()
        if user is not None:
            messages.warning(request, 'Email đã tồn tại!')
        else:
            # luu thong tin nguoi dung moi vao bang nguoi dung
            NguoiDung.objects.create(ho_va_ten=username, email=email, so_dien_thoai=sdt, mat_khau=password)
            messages.success(request, 'Đăng ký thành công!')
    return render(request, 'auth/register.html')
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # kiem tra xem email co ton tai trong bang nguoi dung khong
        user = NguoiDung.objects.filter(email=email).first()
        if user is None:
            messages.warning(request, 'Email không tồn tại!')
        else:
            messages.success(request, 'Mật khẩu của bạn là: ' + user.mat_khau)
    return render(request, 'auth/forgot-password.html')
def cart(request):
    # lay danh sach san pham trong gio hang
    list_cart = request.session.get('list_products_in_cart')
    if list_cart is None:
        list_cart = []
    # tinh tong tien
    total_price = 0
    # dem so luong san pham
    total_quantity = 0
    for item in list_cart:
        total_quantity = total_quantity + item['quantity']
        total_price = total_price + item['price'] * item['quantity']
    #format total price
    total_price = "{:,.2f}".format(total_price)
    # luu lai danh sach san pham trong gio hang
    context = {
        'list_cart': list_cart,
        'total_price': total_price,
        'total_quantity': total_quantity
    }
    return render(request, 'app/cart.html', context)
def checkout(request):
    # kiem tra xem nguoi dung co dang nhap chua
    if 'ID' not in request.session:
        return redirect('login')
    # lay danh sach san pham trong gio hang
    list_cart = request.session.get('list_products_in_cart')
    if list_cart is None:
        list_cart = []
    # tinh tong tien
    total_price = 0
    # dem so luong san pham
    total_quantity = 0
    for item in list_cart:
        total_quantity = total_quantity + item['quantity']
        total_price = total_price + item['price'] * item['quantity']
    #format total price
    total_price = "{:,.2f}".format(total_price)
    # luu lai danh sach san pham trong gio hang
    context = {
        'list_cart': list_cart,
        'total_price': total_price,
        'total_quantity': total_quantity
    }
    return render(request, 'app/checkout.html', context)
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
    #dem so luong nguoi dung
    total_user = NguoiDung.objects.count()
    context = {
        'home_admin': '',
        'total_user': total_user
    }
    return render(request, 'manage_app/base.html', context)
def manage_user(request):
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    if request.method == "POST":
        # lay thong tin tu form
        ho_va_ten = request.POST.get('name')
        ngay_sinh = request.POST.get('date')
        so_dien_thoai = request.POST.get('phone')
        email = request.POST.get('email')
        mat_khau = request.POST.get('password')
        dia_chi = request.POST.get('address')
        vai_tro = request.POST.get('role')
        if request.POST.get('id') != '':
            id = request.POST.get('id')
            # cap nhat thong tin nguoi dung
            NguoiDung.objects.filter(id=id).update(ho_va_ten=ho_va_ten, ngay_sinh=ngay_sinh, so_dien_thoai=so_dien_thoai, email=email, mat_khau=mat_khau, dia_chi=dia_chi, vai_tro=vai_tro)
            # thong bao cap nhat thanh cong
            messages.success(request, 'Cập nhật thành công!')
        else:
            # them moi nguoi dung
            NguoiDung.objects.create(ho_va_ten=ho_va_ten, ngay_sinh=ngay_sinh, so_dien_thoai=so_dien_thoai, email=email, mat_khau=mat_khau, dia_chi=dia_chi, vai_tro=vai_tro)
            # thong bao them moi thanh cong
            messages.success(request, 'Thêm mới thành công!')
    users = NguoiDung.objects.all() # lay tat ca du lieu trong bang nguoi dung
    context = {
        'users': users
    }
    return render(request, 'manage_app/manage_user.html', context)

#delete user
def delete_user(request, id):
    check =  NguoiDung.objects.filter(id=id).delete()
    if check:
        messages.success(request, 'Xóa người dùng thành công!')
    else:
        messages.error(request, 'Xóa người dùng thất bại!')
    return redirect('manage-user')


def manage_product(request):
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    all_products = SanPham.objects.all()
    #lay tat ca loai pham pham loading len select option
    all_categories = LoaiSanPham.objects.all()
    if request.method == "POST":
        #lay thong tin tu form
        id = request.POST.get('ID')
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        quantity = request.POST.get('quantity')
        url = request.POST.get('url')
        type_product = request.POST.get('type_product')
        print("id", id)
        print("name", name)
        print("price", price)
        print("desc", desc)
        print("quantity", quantity)
        print("type_product", type_product)
        print("url", url)
        if id != '':
            #cap nhat thong tin san pham
            check = SanPham.objects.filter(id=id).update(ten_san_pham=name, gia_san_pham=price, mo_ta_san_pham=desc, so_luong_san_pham=quantity, id_loai_san_pham=type_product, hinh_anh_san_pham=url)
            #thong bao cap nhat thanh cong
            if check:
                messages.success(request, 'Cập nhật sản phẩm thành công!')
            else:
                messages.error(request, 'Cập sản phẩm nhật thất bại!')
        else:
            #them moi san pham
            isinstance_loai_san_pham = LoaiSanPham.objects.filter(id=type_product).first()
            SanPham.objects.create(ten_san_pham=name, gia_san_pham=price, mo_ta_san_pham=desc, so_luong_san_pham=quantity, id_loai_san_pham=isinstance_loai_san_pham, hinh_anh_san_pham=url)
            #thong bao them moi thanh cong
            check = messages.success(request, 'Thêm mới thành công!')
            if check:
                messages.success(request, 'Thêm mới sản phẩm thành công!')
            else:
                messages.error(request, 'Thêm mới sản phẩm thất bại!')
           
    context = {
        'products': all_products,
        'categories': all_categories
    }
    return render(request, 'manage_app/manage_product.html', context)
def delete_product(request, id):
    check =  SanPham.objects.filter(id=id).delete()
    if check:
        messages.success(request, 'Xóa sản phẩm thành công!')
    else:
        messages.error(request, 'Xóa sản phẩm thất bại!')
    return redirect('manage-product')
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

def manage_category(request):
    if 'ID' not in request.session or request.session['vai_tro'] != 'admin':
        return redirect('login')
    if request.method == "POST":
        # lay thong tin tu form
        name = request.POST.get('name')
        if request.POST.get('id') != '':
            id = request.POST.get('id')
            # cap nhat thong tin loai san pham
            check = LoaiSanPham.objects.filter(id=id).update(ten_loai_san_pham=name)
            # thong bao cap nhat thanh cong
            if check:
                messages.success(request, 'Cập nhật loại sản phẩm thành công!')
            else:
                messages.error(request, 'Cập nhật loại sản phẩm thất bại!')
        else:
            # them moi loai san pham
            check =  LoaiSanPham.objects.create(ten_loai_san_pham=name)
            if check:
                messages.success(request, 'Thêm mới loại sản phẩm thành công!')
            else:
                messages.error(request, 'Thêm loại sản phẩm mới thất bại!')
    # lay tat ca loai san pham
    categories = LoaiSanPham.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'manage_app/manage_category.html', context)


def delete_category(request, id):
    check =  LoaiSanPham.objects.filter(id=id).delete()
    if check:
        messages.success(request, 'Xóa loại sản phẩm thành công!')
    else:
        messages.error(request, 'Xóa loại sản phẩm thất bại!')
    return redirect('manage-category')

def add_product_to_cart(request, id):
    # lay so luong san pham
    quantity = 1
    # lay danh sach san pham trong gio hang
    list_cart = request.session.get('list_products_in_cart')
    if list_cart is None:
        list_cart = []
    # lay thong tin san pham
    product = SanPham.objects.filter(id=id).first()
    # kiem tra xem san pham da co trong gio hang chua
    for item in list_cart:
        if item['id'] == id:
            item['quantity'] = item['quantity'] + quantity
            break
    else:
        list_cart.append({
            'id': product.id,
            'name': product.ten_san_pham,
            'price': float(product.gia_san_pham),
            'quantity': quantity,
            'image': product.hinh_anh_san_pham
        })
    # luu lai danh sach san pham trong gio hang
    request.session['list_products_in_cart'] = list_cart

    for item in list_cart:
        # in ra ten san pham va so luong
        print(item['name'], item['quantity'])
    
    # dieu huong ve trang gio hang
    return redirect('cart')

def minus_product_to_cart(request, id):
    # neu so luong bang 1 thi xoa san pham do khoi gio hang
    # lay danh sach san pham trong gio hang
    list_cart = request.session.get('list_products_in_cart')
    if list_cart is None:
        list_cart = []
    for item in list_cart:
        if item['id'] == id:
            if item['quantity'] == 1:
                list_cart.remove(item)
            else:
                item['quantity'] = item['quantity'] - 1
            break
    # luu lai danh sach san pham trong gio hang
    request.session['list_products_in_cart'] = list_cart
    # dieu huong ve trang gio hang
    return redirect('cart')

# xoa san pham khoi gio hang
def delete_product_in_cart(request, id):
    # lay danh sach san pham trong gio hang
    list_cart = request.session.get('list_products_in_cart')
    if list_cart is None:
        list_cart = []
    for item in list_cart:
        if item['id'] == id:
            list_cart.remove(item)
            break
    # luu lai danh sach san pham trong gio hang
    request.session['list_products_in_cart'] = list_cart
    # dieu huong ve trang gio hang
    return redirect('cart')

def logout(request):
    # xoa session
    request.session.flush()
    return redirect('login')

    

    