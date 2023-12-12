from django.urls import path

from . import views

# from .views import login

urlpatterns = [
    path("", views.index, name="search"),
    # path("login/", login, name="login"),
]
