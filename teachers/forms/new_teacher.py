from django import forms

from teachers.models import Teacher


class NewTeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['name']
