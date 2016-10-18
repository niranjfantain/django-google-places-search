from __future__ import unicode_literals

from django.db import models


class Trial(models.Model):
    place = models.CharField(max_length=50)
