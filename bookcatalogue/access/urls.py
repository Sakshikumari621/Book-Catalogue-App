from django.urls import path
from access.views import *

# from access.views import signup
# from access.views import signout
# from access.views import book_list
# from access.views import add_book
# from access.views import edit_book
# from access.views import delete_book

from access.views import home

urlpatterns = [
    path("home/", home, name="home"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
    path("book_list/", book_list, name="book_list"),
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", delete_book, name="delete_book"),
    path("public_review/", get_public_review, name="public_review"),
]
