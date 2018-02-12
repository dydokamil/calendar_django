from django.contrib.auth.models import User
from django.db import models


class CalendarEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    date = models.DateField(null=False)

    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
