from django.contrib import admin
from .models import Category, Vegetable

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'weight', 'offer')

