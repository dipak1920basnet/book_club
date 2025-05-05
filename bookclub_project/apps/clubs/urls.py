from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "clubs"
urlpatterns = [
    path("",views.club_list, name="clublist"),
    path("myclub", views.my_club, name="my_club"),
    path("create_club", views.create_club, name="create_club")
]