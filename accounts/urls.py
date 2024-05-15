from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("", include("django.contrib.auth.urls")),
]
