from django.contrib import admin
from .models import Product , Category , Wishlist

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass