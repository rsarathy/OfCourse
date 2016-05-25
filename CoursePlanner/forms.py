from django import forms
from django.contrib.auth.models import User
from CoursePlanner.models import Course
import re

__author__ = 'rohit'

class CourseForm(forms.Form):
    course = forms.CharField(max_length=10, required=False)

    def __str__(self):
        return self.course

    def clean_course(self):
        course = self.cleaned_data["course"]
        cu = re.search('([a-zA-z]{2,4})( ?[0-5][0-9]{2})$', course)
        if cu is None:
	        raise forms.ValidationError("Invalid course. Enter a course in one of the following formats: SUBJ 123, SUBJ123, subj 123, subj123.\n")

        ident = cu.group(1).upper() + " " + cu.group(2).strip()
        query = Course.objects.filter(identifier=ident)
        if len(query) == 0:
            raise forms.ValidationError("That course does not exist.")
        return query[0]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=24, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False))

MAJORS = (
    ('cs', 'Computer Science'),
    ('ce', 'Computer Engineering'),
    ('ee', 'Electrical Engineering'),
)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=24, required=True)
    password = forms.CharField(min_length=8, max_length=32, widget=forms.PasswordInput(render_value=False), required=True)
    conf_pwd = forms.CharField(min_length=8, label=(u'Confirm Password'), max_length=32, widget=forms.PasswordInput(render_value=False), required=True)
    email    = forms.EmailField(max_length=64, required=True)
    major    = forms.ChoiceField(choices=MAJORS)

    def clean_username(self):
        userid = self.cleaned_data["username"]
        if re.search("[a-z0-9_-]{6,24}$", userid) is None:
            raise forms.ValidationError("Username must have 6-24 alphanumeric characters.")
        if User.objects.filter(username=userid).exists():
            raise forms.ValidationError("Username already taken.")
        return userid

    def clean_conf_pwd(self):
        password = self.cleaned_data["password"]
        conf_pwd = self.cleaned_data["conf_pwd"]
        if password and conf_pwd and password != conf_pwd:
            raise forms.ValidationError("Passwords do not match.")
        return conf_pwd

    def clean_email(self):
        em = self.cleaned_data["email"]
        if User.objects.filter(email=em).exists():
            raise forms.ValidationError("Email is already currently in use.")
        return em

    class Meta:
        ordering = ["username"]