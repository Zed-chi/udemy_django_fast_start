from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from pizzashopapp.forms import UserForm, PizzaShopForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home(req):
    return redirect(back_home)


@login_required(login_url="/pizzashopapp/sign-in")
def back_home(req):
    return render(req, "pizzashopapp/home.html")


def sign_up(req):
    user_form = UserForm()
    pizza_shop_form = PizzaShopForm()
    if req.method == "POST":
        user_form = UserForm(req.POST)
        pizza_shop_form = PizzaShopForm(req.POST, req.FILES)
        if user_form.is_valid() and pizza_shop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizza_shop_form.save(commit=False)
            new_pizzashop.owner = new_user
            new_pizzashop.save()
            login(
                req,
                authenticate(
                    username=user_form.cleaned_data["username"],
                    password=user_form.cleaned_data["password"],
                ),
            )
            return redirect(back_home)

    return render(
        req,
        "pizzashopapp/sign_up.html",
        {"user_form": user_form, "pizza_shop_form": pizza_shop_form},
    )


@login_required(login_url="/pizzashopapp/sign-in")
def account(req):
    return render(req, "pizzashopapp/account.html")


@login_required(login_url="/pizzashopapp/sign-in")
def pizza(req):
    return render(req, "pizzashopapp/pizza.html")
