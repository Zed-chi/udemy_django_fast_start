"""pizzashopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizzashopapp.views import home
from pizzashopapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path(
        "pizzashopapp/sign-in/", 
        auth_views.LoginView.as_view(
            template_name="pizzashopapp/sign_in.html"
        ), 
        name="sign_in"
    ),
    path(
        "pizzashopapp/sign-out/", 
        auth_views.LogoutView.as_view(
            next_page="/"
        ), 
        name="sign_out"
    ),
    path(
        "pizzashopapp/", 
        views.back_home, 
        name="back_home"
    ),
    path(
        "pizzashopapp/sign-up", 
        views.sign_up, 
        name="sign_up"
    )
]
