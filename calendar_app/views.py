# Create your views here.
from rest_framework import mixins, generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from calendar_app.models import CalendarEntry
from calendar_app.serializers import CalendarEntryCreateSerializer, \
    CalendarEntryDetailsSerializer, CalendarEntrySerializer


class CalendarEntryView(viewsets.ModelViewSet):
    queryset = CalendarEntry.objects.all()
    serializer_class = CalendarEntryDetailsSerializer
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
        try:
            calendar_entry = CalendarEntry.objects.create(
                label=request.data['label'],
                datetime=request.data['datetime'],
                user=request.user
            )
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = CalendarEntrySerializer(calendar_entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
