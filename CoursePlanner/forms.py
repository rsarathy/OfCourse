from django import forms
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
    email    = forms.EmailField(max_length=64, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False))
    conf_pwd = forms.CharField(label=(u'Confirm Password'), max_length=32, widget=forms.PasswordInput(render_value=False))
    major    = forms.ChoiceField(choices=MAJORS)

    # def clean_signup(self):
    #     password = self.cleaned_data["password"]
    #     confirmp = self.cleaned_data["conf_pwd"]
    #
    #     if password != confirmp:
    #         raise forms.ValidationError("Passwords do not match.")

    class Meta:
        ordering = ["username"]