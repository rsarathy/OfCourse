from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render
from CoursePlanner.forms import *
from CoursePlanner.models import Course

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
    if request.method == 'POST' and "Remove" not in request.POST.values():
        form = CourseForm(request.POST)
        if 'save_semester' in request.POST:
            return save_semester(request)
        if form.is_valid():
            c = form.cleaned_data["course"]
            ident = str(c)
            if 'add_course' in request.POST:
                query = Course.objects.filter(identifier=ident)
                if len(query) == 0:
                    errors.append("That course does not exist.")
                elif query[0] in d[i]:
                    errors.append("You are already taking that class this semester.")
                else:
                    d[i].append(query[0])
                    d[i].sort(key=lambda x: x.identifier)
                    cr[i] += query[0].get_credit()
    elif request.method == 'POST' and "Remove" in request.POST.values():   #removal
        cin = sorted(request.POST)
        to_remove = str(cin[1][7:])
        for c in d[i]:
            if c.identifier == to_remove:
                d[i].remove(c)
                cr[i] -= c.get_credit()
                break
        form = CourseForm()
    else:
        form = CourseForm()
    return render(request, "selection.html",
        {
        "form": form,
        "courses": d[i],
        "errors": errors,
        "credit": cr[i],
        "sem_number": i+1,
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