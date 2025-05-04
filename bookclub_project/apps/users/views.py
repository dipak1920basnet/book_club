from django.shortcuts import render
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from .models import Users


import traceback
import logging
from django.core.exceptions import ObjectDoesNotExist

# logging.basicConfig(
#     level=logging.INFO,
#     filename="finance.log",
#     filemode="a",
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )

def index(request):
    return render(request, "home.html",
                  {
                      "username":request.user
                  })

def login_view(request):
    if request.method == "POST":
        user_email = request.POST.get("user_email")
        password = request.POST.get("user_password")

        # Get user name by email
        try:
            user= Users.objects.get(email=user_email)

        except Users.DoesNotExist:
            return render(request, "login.html",
                          {
                            "error_message" : "User does not exits"
                          })
        
        else:
            user = authenticate(request, username=user.username, password= password)
            if user:
                login(request, user=user)
                return redirect('users:index')
            else:
                return render(request, "login.html",
                            {
                                "error_message" : "Please enter correct password"
                            })
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        new_email = request.POST.get("Email")
        password = request.POST.get("Password")

        user = Users.objects.filter(email=new_email).exists()
        # except Users.DoesNotExist:
        if not user:
            m = Users.objects.create_user(username=username,email=new_email,password=password)
            m.save()
            new_user = authenticate(request, username=username, password= password)
            if new_user:
                login(request, new_user )
                return redirect('users:index')
        else:
            user = Users.objects.get(email=new_email)
            existing_user = authenticate(request, username=user.username, password= password)
            if existing_user:
                login(request, existing_user)
                return redirect('users:index')
                
            return render(request, "register.html", 
                        {
                            "message":"User already exists please choose different email"
                        })
    return render(request, "register.html")

@login_required
def my_club(request):
    return render(request, "my_clubs.html")

@login_required
def settings(request):
    return render(request, "settings.html")

# @login_required
def Logout(request):
    logout(request)
    return redirect('users:index')