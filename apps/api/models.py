from datetime import date, time
from django.db import models
from apps.authentication.models import User


# Create your models here.
class Event(models.Model):
    class Meta:
        verbose_name_plural = 'events'

    # TODO: only admin can make event

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # TODO: add image field to upload image
    flyer = models.TextField(max_length=300, default='', blank=True)
    type = models.CharField(max_length=100)
    # TODO: change to DateField possibly
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    # TODO: add array of users field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: events can have attendance and sessions can have attendance, but can't have both at a time
    event = models.ForeignKey(Event, related_name='attendances', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

#
# class Session(models.Model):
#     class Meta:
#         verbose_name_plural = 'sessions'
#
#     # TODO: Sessions should be auto-generated, but admin can also make events
#
#     category = models.CharField(max_length=100)  # beginner, intermediate, advanced
#     date = models.DateField()  # date of scheduled class
#     time = models.TimeField()  # time of scheduled class
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
## TODO: can both attendance can be merged
# class SessionAttendance(models.Model):
#
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     # TODO: events can have attendance and sessions can have attendance, but can't have both at a time
#     session = models.ForeignKey(Session, related_name='session_attendances', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name

