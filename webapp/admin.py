from django.contrib import admin
from webapp.models import Category, Product

# Register your models here.
@admin.register(Category)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name', 'description']

@admin.register(Product)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'date', 'price', 'imagine']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name', 'description', 'category', 'date', 'price', 'imagine']
    readonly_fields = ['date']
