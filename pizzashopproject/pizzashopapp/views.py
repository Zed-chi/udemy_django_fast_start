from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    return redirect(back_home)

@login_required(login_url="/pizzashopapp/sign-in")
def back_home(req):
    return render(req, "pizzashopapp/home.html")


def sign_up(req):
    return render(req, "pizzashopapp/sign_up.html")