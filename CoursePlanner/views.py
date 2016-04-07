from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from CoursePlanner.forms import *
from django.forms import forms
from courses import Course, Catalog

all_courses = Catalog("courses.txt").get_courses()

d = []
cr = [0, 0, 0, 0, 0, 0, 0, 0] # 8 semesters of credit

def add_course(request):
    errors = []
    c = ""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data["course"]
            course_ = str(c)
            if 'save_semester' in request.POST:
                return save_semester(request)
            elif course_ in d:
                errors.append("You are already taking that class.")
            elif 'add_course' in request.POST:
                d.append(str(course_))
                d.sort()
                if course_ in all_courses:
                    cr[0] += int(all_courses[course_].get_credit())
    else:
        form = CourseForm()
    return render(request, "selection.html",
                  {"form": form, "courses": d, "errors": errors, "credit": cr[0]})


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

# incomplete error checking
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
    return render(request, "signup.html", {"form": form, "errors": errors})

def save_semester(request):
    return render(request, "semesters.html", {"courses": d, "credit": cr[0], "cr_hours": sum(cr)})

def plans(request):
    pass