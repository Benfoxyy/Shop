from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('add_product', views.add_product_view, name='add'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('product/<int:pk>', views.product_view, name='single'),
    path('product/<str:cat>', views.index_view, name='category'),
    path('wishlist', views.wishlist_view, name='wishlist'),
    path('add_wishlist', views.add_wishlist_view, name='add_wishlist'),
]
