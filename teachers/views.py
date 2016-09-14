from django.shortcuts import render

from .models import Teacher
from .forms.new_teacher import NewTeacherForm
from lessons.forms.new_lesson import NewLessonForm

def index(request):

    if request.method == 'POST':
        new_teacher_form = NewTeacherForm(data=request.POST)
        if new_teacher_form.is_valid():
            teacher = new_teacher_form.save()
            new_teacher_form = NewTeacherForm()
    else:
        new_teacher_form = NewTeacherForm()

    teachers = Teacher.objects.all()
    new_lesson_form = NewLessonForm()

    return render(request, 'teachers_index.html', context={
        'teachers': teachers,
        'new_teacher_form': new_teacher_form,
        'new_lesson_form': new_lesson_form
    })
