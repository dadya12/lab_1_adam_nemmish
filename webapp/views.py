from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Category, Product
from django.http import HttpResponseRedirect
from webapp.forms import ProductForm
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
        form = ProductForm()
        return render(request, 'create_product.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                category=form.cleaned_data.get('category'),
                price=form.cleaned_data.get('price'),
                remainder=form.cleaned_data.get('remainder'),
                imagine=form.cleaned_data.get('imagine'),
            )
            return redirect('product_views', pk=product.pk)
        else:
            return render(request, 'create_product.html', {'form': form})

def update_product(request, pk):
    products = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            'name': products.name,
            'description': products.description,
            'category': products.category,
            'price': products.price,
            'remainder': products.remainder,
            'imagine': products.imagine
        })
        return render(request, 'update_product.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            products.name = form.cleaned_data.get('name')
            products.description = form.cleaned_data.get('description')
            products.category = form.cleaned_data.get('category')
            products.price = form.cleaned_data.get('price')
            products.remainder = form.cleaned_data.get('remainder')
            products.imagine = form.cleaned_data.get('imagine')
            products.save()
            return redirect('home')
        else:
            products.save()
            return render(request, 'update_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_product.html', {'product': product})
    elif request.method == "POST":
        product.delete()
        return redirect('home')
