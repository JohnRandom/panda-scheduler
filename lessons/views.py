from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms.new_lesson import NewLessonForm
from .models import Lesson
from teachers.models import Teacher
from students.forms.new_student import NewStudentForm


def index(request):
    teachers = Teacher.objects.all()

    return render(request, 'lessons_index.html', context={
        'teachers': teachers,
        'new_student_form': NewStudentForm()
    })


def new_lesson(request, teacher_id):

    if request.method == 'POST':
        teacher = Teacher.objects.get(id=teacher_id)
        lesson = Lesson(teacher=teacher)
        form = NewLessonForm(instance=lesson, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers.views.index'))
        else:
            return render(request, 'new_lesson.html', context={
                'form': form
            })
    else:
        form = NewLessonForm()
        return render(request, 'new_lesson.html', context={
            'form': form
        })
