from django.shortcuts import render


def home(req):
    return render(req, "home.html", {})

def user(req, id):
    return render(req, "home.html", {})