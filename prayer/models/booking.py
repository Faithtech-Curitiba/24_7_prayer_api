from django.db import models
from prayer.mixins import ModelMixin
from django.conf import settings

settings.DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S%z'

class Booking(ModelMixin):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    datetime = models.DateTimeField(unique=True)
