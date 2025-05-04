from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
    path("",views.index, name = "index"),
    path("login_view", views.login_view, name="login_view"),
    path("register_view", views.register_view, name="register_view"),
    path("my_club", views.my_club, name="my_club"),
    path("settings",views.settings, name="settings"),
    path("logout",views.Logout, name="logout")
]