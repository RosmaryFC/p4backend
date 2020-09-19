from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.api.models import Event, Attendance
from apps.api.serializers import EventSerializer, AttendanceSerializer


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    # user must be logged in to create event
    # TODO: figure out how to check if user is admin
    permission_classes = (IsAuthenticated,)
    # used to convert data back and forth
    serializer_class = EventSerializer

    # TODO: get all events should be allowed with no authentication
    def get_queryset(self):
        # this one filters by user id
        # queryset = Event.objects.all().filter(owner=self.request.user)
        # TODO: changed! Test -> every user can get all events
        queryset = Event.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        event = Event.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if event:
            msg = 'Event with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # TODO: right now, user can only delete category they created, make it so that admins can delete category
    # TODO: delete does not return a response!!
    def destroy(self, request, *args, **kwargs):
        event = Event.objects.get(pk=self.kwargs["pk"])
        serializer = self.get_serializer(self.get_object())
        if not request.user == event.owner:
            raise PermissionDenied("you cannot delete this event")
        super().destroy(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return super().destroy(request, *args, **kwargs)


class EventAttendances(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        if self.kwargs.get("event_pk"):
            event = Event.objects.get(pk=self.kwargs["event_pk"])
            # TODO: if admin, can see all attendance, if not, can only see their attendance
            queryset = Attendance.objects.filter(
                # owner=self.request.user,
                event=event
            )
            return queryset

    def perform_create(self, serializer):
        serializer.view(owner=self.request.user)


class SingleEventAttendance(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        if self.kwargs.get("event_pk") and self.kwargs.get("pk"):
            event = Event.objects.get(pk=self.kwargs["event_pk"])
            queryset = Attendance.objects.filter(
                pk=self.kwargs["pk"],
                owner=self.request.user,
                event=event
            )
            return queryset


class AttendancesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = Attendance.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create attendance"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        attendance = Attendance.objects.get(pk=self.kwargs["pk"])
        # TODO: only admin can destroy an attendance
        if not request.user == attendance.owner:
            raise PermissionDenied(
                "you have no permission to delete this attendance"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        attendance = Attendance.objects.get(pk=self.kwargs["pk"])
        # TODO: only admin can update an attendance - might not need this
        if not request.user == attendance.owner:
            raise PermissionDenied(
                "you have no permissions to edit this attendance"
            )
        return super().update(request, *args, **kwargs)
