from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['seller', 'name', 'description', 'price', 'address','pic']

        widgets = {
            'seller' : forms.TextInput(attrs={'class': 'form-control','type': 'hidden'}),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']