from django.contrib import admin
from .models import Product , Category

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass