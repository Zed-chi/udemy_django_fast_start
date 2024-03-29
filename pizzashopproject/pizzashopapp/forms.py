from django import forms
from django.contrib.auth.models import User
from pizzashopapp.models import PizzaShop


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")


class PizzaShopForm(forms.ModelForm):
    class Meta:
        model = PizzaShop
        fields = ("name", "phone", "address", "logo")
