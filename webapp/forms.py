from django import forms
from webapp.models import Product
from django.forms import widgets

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'reminder', 'image']
