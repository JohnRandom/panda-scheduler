from django.db import models
from django.utils import timezone


class LessonsManager(models.Manager):

    def cancelled(self):
        return self.get_queryset.filter(cancelled=True)

    def active(self):
        return self.get_queryset.filter(cancelled=False)

