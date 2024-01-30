from django.urls import path
from access.views import signin
from access.views import signup
from access.views import signout

from access.views import home

urlpatterns = [
    path("home/", home, name="home"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
]
