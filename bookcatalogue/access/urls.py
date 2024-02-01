from django.urls import path
from access.views import signin
from access.views import signup
from access.views import signout
from access.views import book_list
from access.views import add_book

from access.views import home

urlpatterns = [
    path("home/", home, name="home"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
    path("book_list/", book_list, name="book_list"),
    path("add_book/", add_book, name="add_book"),
]
