

from django.db.models import IntegerField, Model, JSONField
from django.db import models


class Config(models.Model):
    userId = models.IntegerField(primary_key = True)
    selected_duties = JSONField()
    selected_staff = JSONField()