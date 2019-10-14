from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from pizzashopapp.forms import UserForm, PizzaShopForm

# Create your views here.
def home(req):
    return redirect(back_home)


@login_required(login_url="/pizzashopapp/sign-in")
def back_home(req):
    return render(req, "pizzashopapp/home.html")


def sign_up(req):
    user_form = UserForm()
    pizza_shop_form = PizzaShopForm()

    return render(
        req, 
        "pizzashopapp/sign_up.html",
        {
            "user_form":user_form,
            "pizza_shop_form": pizza_shop_form
        }
    )
