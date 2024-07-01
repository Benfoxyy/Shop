from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('product/<int:pk>/', views.product_view, name='single'),
    path('product/<str:cat>/', views.index_view, name='category'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('delete/<str:name>/', views.delete_wish, name='delete'),
    path('add_wishlist/<int:wish>/', views.add_wishlist_view, name='add_wishlist'),
    path('success/', views.success_view, name='success'),
]
