"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import home, product_views, create_category, create_product, update_product, delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', home, name='product'),
    path('products/<int:pk>/', product_views, name='product_views'),
    path('categories/add', create_category, name='create_category'),
    path('products/add', create_product, name='create_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product')
]
