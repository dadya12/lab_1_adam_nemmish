from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Category, Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

