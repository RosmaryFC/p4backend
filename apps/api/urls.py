from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import EventViewSet, AttendancesViewSet, SingleEventAttendance, EventAttendances, EventViewSetPublic

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('attendances', AttendancesViewSet, basename='attendances')
router.register('eventspublic', EventViewSetPublic, basename='eventspublic')

custom_urlpatterns = [
   url(r'events/(?P<event_pk>\d+)/attendances$', EventAttendances.as_view(), name='event_attendances'),
   url(r'events/(?P<event_pk>\d+)/attendances/(?P<pk>\d+)/$', SingleEventAttendance.as_view(),
       name='single_event_attendance')
]
urlpatterns = router.urls
urlpatterns += custom_urlpatterns

# urlpatterns = [
#     path('', include(router.urls))
# ]