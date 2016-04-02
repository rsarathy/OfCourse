from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from CoursePlanner.forms import *
from django.forms import forms

d = []
def add_course(request):
    errors = []
    c = ""
    save = SaveForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data["course"]
            course_ = str(c)
            if 'save_semester' in request.POST:
                return render(request, "semesters.html", {"courses": d})
            elif course_ in d:
                errors.append("You are already taking that class.")
            elif 'add_course' in request.POST:
                d.append(str(course_))
                d.sort()
                return render(request, "selection.html",
                    {"form": form, "courses": d})

    else:
        form = CourseForm()
    return render(request, "selection.html",
                  {"save": save, "form": form, "courses": d, "errors": errors})

def login(request):
    userid = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data["username"]
            passwd = form.cleaned_data["password"]
            return render(request, "index.html", {"username": userid})
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form, "username": userid})

# incomplete error checking
def signup(request):
    errors = []
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data["username"]
            passwd = form.cleaned_data["password"]
            confpd = form.cleaned_data["conf_pwd"]

            # controlflow bugs
            if len(passwd) < 8:
                errors.append("Password must be at least 8 characters.")
            if passwd != confpd:
                errors.append("Passwords do not match.")

            return render(request, "index.html", {"username": userid})
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form, "errors": errors})