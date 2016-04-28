from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, render_to_response
from CoursePlanner.forms import *

def login(request):
    userid = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data["username"]
            passwd = form.cleaned_data["password"]
            user = authenticate(username=userid, password=passwd)
            if user is not None and user.is_active:
                return render(request, "index.html", {"username": userid})
            else:
                print "Invalid login."
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form, "username": userid})

def signup(request):
    errors = []
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data["username"]
            email  = form.cleaned_data["email"]
            passwd = form.cleaned_data["password"]
            confpd = form.cleaned_data["conf_pwd"]

            # controlflow bugs
            if len(passwd) < 8:
                errors.append("Password must be at least 8 characters.")
            elif passwd != confpd:
                errors.append("Passwords do not match.")
            else:
                user = User.objects.create_user(userid, email, passwd)
                user.save()
                # send_mail("Please verify your OfCourse Account",
                #           "Thank you for registering with OfCourse.",
                #           "rohit@sarathy.org", [email])
                return render(request, "index.html", {"username": userid})
    else:
        form = SignupForm()
    return render(request, "signup.html",
        {
        "form": form,
        "errors": errors,
        })