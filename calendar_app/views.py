# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from calendar_app.models import CalendarEntry
from calendar_app.serializers import CalendarEntrySerializer


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

        if 'year' in request.GET:
            queryset = queryset.filter(start_datetime__year=request.GET['year'])

        if 'month' in request.GET:
            queryset = queryset.filter(
                start_datetime__month=request.GET['month']
            )

        if 'day' in request.GET:
            queryset = queryset.filter(start_datetime__day=request.GET['day'])

        serializer = CalendarEntrySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print({**request.data, "user": request.user.id})
        serializer = CalendarEntrySerializer(
            data={**request.data, 'user': request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
