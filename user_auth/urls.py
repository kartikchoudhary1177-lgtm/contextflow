from django.contrib import admin
from django.urls import path
from user_auth.views import SignUp,SignIn

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/",SignUp.as_view()),
    path("signin/",SignIn.as_view())
]
