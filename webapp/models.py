from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    description = models.TextField(max_length=200, verbose_name='Описание', null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=200, verbose_name='Описание', null=True, blank=True)
    category = models.ForeignKey('webapp.Category', verbose_name='Категория', on_delete=models.RESTRICT)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=0)
    imagine = models.CharField(verbose_name='Изображение', max_length=300)
