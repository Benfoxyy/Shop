from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('add_product', views.add_product_view, name='add'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('product/<int:pk>', views.product_view, name='single'),
]
