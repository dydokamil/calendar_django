from django.contrib import admin

# Register your models here.
from calendar_app.models import CalendarEntry

# admin.register(CalendarEntry)
admin.site.register(CalendarEntry)
