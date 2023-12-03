from django.shortcuts import render, get_object_or_404
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
            description= request.POST.get('description'),
        )
        return HttpResponseRedirect('/')

