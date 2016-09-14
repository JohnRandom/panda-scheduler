from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms.new_lesson import NewLessonForm
from teachers.models import Teacher
from .models import Lesson


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
        return render('new_lesson.html', context={
            'form': form
        })
