from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {}
    return render(request, 'app/base.html')
def auth(request):
    context = {}
    return render(request, 'auth/base.html')
def content(request):
    context = {}
    return render(request, 'app/content.html')

