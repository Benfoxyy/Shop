from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib import messages


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                u = form.save()
                login(request, u)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Registration Successfully Complete!",
                )
                return redirect("/")
            else:
                messages.error(
                    request,
                    "Username : Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                )
                messages.error(
                    request,
                    "Password : yor password must contain at least 8 characters. | can't be entirely numeric",
                )
        #                return redirect('shop:sign_up')
        else:
            form = SignupForm()
    return render(request, "registration/sign_up.html", {"form": form})
