from django import forms

from teachers.models import Teacher


class NewTeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(NewTeacherForm, self).__init__(*args, **kwargs)
        self.set_widget_css_class('form-control')

    def set_widget_css_class(self, class_name):
        for field in self.fields.keys():
            self.fields[field].widget.attrs['class'] = class_name
