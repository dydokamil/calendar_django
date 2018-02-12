from django.contrib.auth.models import User
from django.db import models


class CalendarEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
