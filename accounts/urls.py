from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("", include("django.contrib.auth.urls")),
]
