from django.contrib import admin
from django.urls import path
from user_auth.views import SignUp,SignIn

urlpatterns = [
     path("signup/", SignUp.as_view(), name="signup"),
    path("signin/", SignIn.as_view(), name="signin"),
]
