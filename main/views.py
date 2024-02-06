from django.shortcuts import render,redirect,get_object_or_404
from .models import Product , Category , Wishlist
from .forms import ProductForm,SignupForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='login')
def index_view(request,cat=None):
    user = Wishlist.objects.get(user = request.user.id)
    wishs = user.wished_items.all()
    if cat:
        cat = cat.replace('-',' ')
        category = Category.objects.get(name=cat)
        p = Paginator(Product.objects.filter(Category=category),8)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
    
        return render(request, 'shop/index.html',{'products':page_obj, 'category':category,'wishlist':wishs})
    else:
        p = Paginator(Product.objects.all(),8)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)


    
        return render(request, 'shop/index.html',{'products':page_obj,'wishlist':wishs})

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

@login_required(login_url='login')
def product_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    user = Wishlist.objects.get(user = request.user.id)
    wishs = user.wished_items.all()

    return render(request,'shop/single.html',{'prod':product,'wishlist':wishs})

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

@login_required(login_url='login')
def wishlist_view(request):
    user = Wishlist.objects.get(user = request.user.id)
    wishs = user.wished_items.all()

    return render(request, 'wishlist/wishlist.html',{'wishlist':wishs})

@login_required(login_url='login')
def add_wishlist_view(request,wish):
    userr = Wishlist.objects.get(user=request.user.id)
    wishes = userr.wished_items.add(wish)

    return redirect('/')