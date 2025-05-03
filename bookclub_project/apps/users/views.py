from django.shortcuts import render
# Create your views here.

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")

@login_required
def my_club(request):
    return render(request, "my_clubs.html")

@login_required
def settings(request):
    return render(request, "settings.html")