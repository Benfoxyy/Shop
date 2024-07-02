from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Wishlist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index_view(request, cat=None, name=None):
    if request.user.is_authenticated:
        try:
            userr, created = Wishlist.objects.get_or_create(
                users=request.user
            )
            wishs = len(userr.wished_items.all())
        except Wishlist.DoesNotExist:
            wishs = 0
    else:
        wishs = 0
    if cat:
        cat = cat.replace("-", " ")
        category = Category.objects.get(name=cat)
        p = Paginator(Product.objects.filter(Category=category), 8)
        page_number = request.GET.get("page")
        try:
            page_obj = p.get_page(
                page_number
            )  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        return render(
            request,
            "shop/index.html",
            {"products": page_obj, "category": category, "wishss": wishs},
        )
    else:
        p = Paginator(Product.objects.all(), 8)
        page_number = request.GET.get("page")
        try:
            page_obj = p.get_page(
                page_number
            )  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        return render(
            request,
            "shop/index.html",
            {"products": page_obj, "wishss": wishs},
        )


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    try:
        userr = Wishlist.objects.get(users=request.user.id)
        wishs = len(userr.wished_items.all())
    except Wishlist.DoesNotExist:
        wishs = 0

    return render(
        request, "shop/single.html", {"prod": product, "wishss": wishs}
    )


@login_required(login_url="login")
def wishlist_view(request):
    try:
        userr = Wishlist.objects.get(users=request.user.id)
        wishs = len(userr.wished_items.all())
        wishes = userr.wished_items.all()

        total = 0
        for i in wishes:
            total += i.price
    except Wishlist.DoesNotExist:
        wishs = 0
        wishes = []

    return render(
        request,
        "wishlist/wishlist.html",
        {"wishss": wishs, "wishes": wishes, "total": total},
    )


@login_required(login_url="login")
def delete_wish(request, name=None):
    person = request.user.username
    u = Wishlist.objects.get(users__username=person)
    u.wished_items.remove(name)

    return redirect("shop:wishlist")


@login_required(login_url="login")
def add_wishlist_view(request, wish):
    try:
        userr = Wishlist.objects.get(users=request.user.id)
        userr.wished_items.add(wish)
    except Wishlist.DoesNotExist:
        pass

    return redirect("/")


@login_required(login_url="login")
def success_view(request):
    return render(request, "purche/success.html")
