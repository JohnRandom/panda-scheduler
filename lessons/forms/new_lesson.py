from django import forms

from lessons.models import Lesson


class NewLessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = [
            'weekday',
            'time_starting',
            'time_ending',
            'max_attendance',
            'subject',
            'description'
        ]
