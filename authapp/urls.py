from django.urls import path
from .views import home, login, register

app_name = "authapp"
urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("register/", register, name="register")
]
