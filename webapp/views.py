from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Category, Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_views(requset, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(requset, 'products_view.html', {'products': products})

