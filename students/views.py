from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms.new_student import NewStudentForm
from lessons.models import Lesson


def new_student(request, lesson_id):

    lesson = Lesson.objects.get(id=lesson_id)
    if not lesson.seats_available():
        pass
        # Make student aware

    if request.method == 'POST':
        form = NewStudentForm(data=request.POST)

        if form.is_valid():
            student = form.save()
            lesson.students.add(student)
            return HttpResponseRedirect(reverse('lessons.views.index'))
        else:
            return render(request, 'new_student.html', context={
                'form': form
            })
    else:
        form = NewStudentForm()
        return render(request, 'new_student.html', context={
            'form': form
        })

