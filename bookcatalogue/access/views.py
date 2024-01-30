from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    fname = request.GET.get("fname", "")
    messages.success(request, "Login successful!")
    return render(request, "access/index.html", {"fname": fname})


# Create New User
def signup(request):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        e_mail = request.POST["e_mail"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]

        # Check if user already exists
        if User.objects.filter(username=user_name).exists():
            messages.error(request, "Username already exists.")
            return redirect("/signup")

        # Check if passwords match
        if password != c_password:
            messages.error(request, "Passwords do not match.")
            return redirect("/signup")

        new_user = User.objects.create_user(user_name, e_mail, password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        messages.success(request, "Account Created Successfully.")

        return redirect("/signin")

    return render(request, "access/signup.html")


# Login User
def signin(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect("/home?fname=" + fname)
        else:
            print("error")
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("/signin")
    return render(request, "access/signin.html")


# Logout User
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("/signin")
