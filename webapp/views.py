from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Category, Product
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_views(requset, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(requset, 'products_view.html', {'products': products})

def create_category(request):
    if request.method == "GET":
        return render(request, 'create_category.html')
    elif request.method == "POST":
        category = Category.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return HttpResponseRedirect('/')

def create_product(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'categories': categories})
    elif request.method == "POST":
        product = Product.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            imagine=request.POST.get('imagine'),
            category_id=request.POST.get('category_id'),
            description=request.POST.get('description'),
        )
        return redirect('product_views', pk=product.pk)
