from rest_framework import serializers

from calendar_app.models import CalendarEntry


# class CalendarEntryCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CalendarEntry
#         fields = ('label', 'start_datetime', 'end_datetime')


class CalendarEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEntry
        fields = '__all__'


# class CalendarEntryDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CalendarEntry
#         fields = ('user', 'label', 'datetime')
