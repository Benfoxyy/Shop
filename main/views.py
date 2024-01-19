from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm,SignupForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def index_view(request):
    products=Product.objects.all()
    return render(request, 'shop/index.html',{'products':products})

@login_required(login_url='login')
def add_product_view(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.seller = request.user
            obj.save()
            messages.success(request, 'Product added successfully!')
            return redirect('/')
        else:
            messages.error(request, 'Somthing went wrong! | Please try again correctly')
            return redirect('shop:add')
    form = ProductForm()
    return render(request, 'shop/add_product.html',{'form':form})

def product_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request,'shop/single.html',{'prod':product})

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                messages.add_message(request,messages.SUCCESS,'Registration Successfully Complete!')
                return redirect('/')
            else:
                messages.error(request, 'Somthing went wrong! | Please try again correctly')
                return redirect('shop:sign_up')
        form = SignupForm()
    return render(request, 'registration/sign_up.html',{'form':form})