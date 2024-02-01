from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from access.models import Book


@login_required
def home(request):
    fname = request.GET.get("fname", "")
    # messages.success(request, "Login successful!")
    return render(request, "index.html", {"fname": fname})


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

    return render(request, "signup.html")


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
    return render(request, "signin.html")


# Logout User
@login_required
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("/signin")


@login_required
def book_list(request):
    if request.method == "GET":
        book_list = Book.objects.filter(user=request.user)

    return render(request, "book_list.html", {"books": book_list})


@login_required
def add_book(request):
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        author = request.POST.get("author_name")
        year = request.Post.get("release_year")
        description = request.POST.get("description")
        rating = int(request.POST.get("rating"))
        comment = request.POST.get("comment")
        public = request.POST.get("public")
        public = True if public else False
        Book.objects.create(
            book_name=book_name,
            author_name=author,
            year_of_release=year,
            description=description,
            rating=rating,
            comment=comment,
            public=public,
        )
        return redirect("/book_list")
    return render(request, "add_book.html")


@login_required
def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        book.book_name = request.POST.get("book_name")
        book.author_name = request.POST.get("author_name")
        book.year_of_release = request.Post.get("release_year")
        book.description = request.POST.get("description")
        book.rating = int(request.POST.get("rating"))
        book.comment = request.POST.get("comment")
        public = request.POST.get("public")
        book.public = True if public else False
        book.save()
        return redirect("/book_list")
    return render(request, "edit_book.html", {"book": book})


@login_required
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect("/book_list")
