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
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data["username"]
            email  = form.cleaned_data["email"]
            passwd = form.cleaned_data["password"]
            user = User.objects.create_user(userid, email, passwd)
            user.save()
                # send_mail("Please verify your BerryHub Account",
                #           "Thank you for registering with BerryHub.",
                #           "rohit@sarathy.org", [email])
            return render(request, "index.html", {"user": user})
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})