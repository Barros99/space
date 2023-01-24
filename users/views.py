from django.shortcuts import render
from users.forms import LoginForms


def login(request):
    form = LoginForms()
    return render(request, "users/login.html", {"form": form})


def signup(request):
    return render(request, "users/signup.html")


def logout(request):
    return render(request, "users/logout.html")
