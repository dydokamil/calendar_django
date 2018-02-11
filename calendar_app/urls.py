from django.urls import path, include
from rest_framework.routers import DefaultRouter

from calendar_app import views

router = DefaultRouter()

router.register('calendar_entry', views.CalendarEntryView)

urlpatterns = [
    path('rest/', include(router.urls)),
]
