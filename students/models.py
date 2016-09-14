from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import UUIDModel


class Student(UUIDModel):

    name = models.CharField(_('name'), max_length=255)
