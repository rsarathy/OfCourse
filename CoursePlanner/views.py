from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from CoursePlanner.forms import CourseForm
from django.forms import forms

d = []
def add_course(request):
    errors = []
    c = ""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data["course"]

            course_ = str(c)

            if course_ in d:
                errors.append("You are already taking that class.")
            else:
                d.append(str(course_))
                return render(request, "selection.html",
                    {"form": form, "courses": d})
    else:
        form = CourseForm()
    return render(request, "selection.html",
                  {"form": form, "courses": d, "errors": errors})

# def home(request):
#     return render(request, "index.html")