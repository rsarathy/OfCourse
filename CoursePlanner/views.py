from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from CoursePlanner.forms import *
from django.forms import forms
from courses import Course, Catalog

all_courses = Catalog("courses.txt").get_courses()

d = [[],[],[],[],[],[],[],[]]
cr = [0, 0, 0, 0, 0, 0, 0, 0] # 8 semesters of credit
urls = {}
for i in range(1,9):
    U = "Semester " + str(i)
    L = "selection" + str(i)
    urls[U] = L

def add_course(request):
    errors = []
    c = ""
    i = int(request.path[-2]) - 1
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if 'save_semester' in request.POST:
            return save_semester(request)
        if form.is_valid():
            c = form.cleaned_data["course"]
            course_ = str(c)
            if 'add_course' in request.POST:
                if course_ in d[i]:
                    errors.append("You are already taking that class this semester.")
                else: #addition
                    d[i].append(str(course_))
                    d[i].sort()
                    if course_ in all_courses:
                        cr[i] += int(all_courses[course_].get_credit())
        else: #removal
            cin = sorted(request.POST)[0][2:]
            if cin in d[i]:
                d[i].remove(cin)
                cr[i] -= int(all_courses[cin].get_credit())
                form = CourseForm()
    else:
        form = CourseForm()
    return render(request, "selection.html",
        {
        "form": form,
        "courses": d[i],
        "errors": errors,
        "credit": cr[i],
        })

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
    return render(request, "login.html",
        {
        "form": form,
        "username": userid,
        })

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
    return render(request, "signup.html",
        {
        "form": form,
        "errors": errors,
        })

def save_semester(request):
    return render(request, "semesters.html",
        {
        "urls": urls,
        "courses": d,
        "credit": cr,
        "cr_hours": sum(cr),
        })

def plans(request):
    pass