from django import forms

from students.models import Student


class NewStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [ 'name' ]
