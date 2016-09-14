from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import UUIDModel
from teachers.models import Teacher
from students.models import Student
from .managers import LessonsManager


WEEKDAY_CHOICES = (
    (0, _('Monday')),
    (1, _('Tuesday')),
    (2, _('Wednesday')),
    (3, _('Thursday')),
    (4, _('Friday')),
    (5, _('Saturday')),
    (6, _('Sunday'))
)


class Lesson(UUIDModel):

    objects = LessonsManager()

    time_starting = models.TimeField(_('time starting'), editable=True)
    time_ending = models.TimeField(_('time ending'), editable=True)
    weekday = models.IntegerField(_('weekday'), choices=WEEKDAY_CHOICES, default=0)
    max_attendance = models.IntegerField(_('max. attendance'), default=10)
    subject = models.CharField(_('subject'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    cancelled = models.BooleanField(_('cancelled'), default=False)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    students = models.ManyToManyField(Student, related_name='students')

    def seats_available(self):
        return max(self.max_attendance - self.students.count(), 0)
