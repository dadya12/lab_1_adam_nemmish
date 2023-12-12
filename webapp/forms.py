from django import forms
from webapp.models import Product, Category
from django.forms import widgets
from django.core.validators import MinValueValidator

class ProductForm(forms.Form):
    name = forms.CharField(label='Наименование', max_length=100, required=True)
    description = forms.CharField(label='Описание', max_length=200, required=True, widget=widgets.Textarea)
    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), required=True)
    price = forms.DecimalField(label='Стоимость',max_digits=7, decimal_places=2, required=True)
    remainder = forms.IntegerField(label='Остаток', validators=[MinValueValidator(0)], required=True)
    imagine = forms.CharField(label='Изображение', max_length=300, required=True)
