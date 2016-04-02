from django import forms
import re

__author__ = 'rohit'

class CourseForm(forms.Form):
    course = forms.CharField(max_length=10, required=True)

    def __str__(self):
        return self.course

    def clean_course(self):
        course = self.cleaned_data["course"]

        cu = re.search('([a-zA-z]{2,4})( ?[0-5][0-9]{2})$', course)
        if cu is None:
	        raise forms.ValidationError("Invalid course. Enter a course in one of the following formats: SUBJ 123, SUBJ123, subj 123, subj123.\n")
        ret = cu.group(1).upper() + " " + cu.group(2).strip()
        return ret

    class Meta:
        ordering = ["course"]

class SaveForm():
    pass

class LoginForm(forms.Form):
    username = forms.CharField(max_length=24, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False))


MAJORS = (
    ('cs', 'Computer Science'),
    ('ce', 'Computer Engineering'),
)
class SignupForm(forms.Form):
    username = forms.CharField(max_length=24, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False))
    conf_pwd = forms.CharField(label=(u'Confirm Password'), max_length=32, widget=forms.PasswordInput(render_value=False))
    major    = forms.ChoiceField(choices=MAJORS)