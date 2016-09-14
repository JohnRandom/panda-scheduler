from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

import uuid


class UUIDModel(models.Model):

    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
