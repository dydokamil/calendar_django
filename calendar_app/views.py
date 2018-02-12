# Create your views here.
from django.core.exceptions import ValidationError
from rest_framework import mixins, generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from calendar_app.models import CalendarEntry
from calendar_app.serializers import CalendarEntrySerializer, \
    CalendarEntryCreateSerializer


class CalendarEntryView(viewsets.ModelViewSet):
    queryset = CalendarEntry.objects.all()
    serializer_class = CalendarEntrySerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        queryset = CalendarEntry.objects.filter(user=request.user)

        serializer = CalendarEntrySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        allowed = ['start_datetime', 'end_datetime', 'label']
        filtered = {
            k: request.data[k] for k in allowed if k in request.data
        }
        try:
            calendar_entry = CalendarEntry.objects.create(
                user=request.user,
                **filtered
            )
        except KeyError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

        serializer = CalendarEntryCreateSerializer(calendar_entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
