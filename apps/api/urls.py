from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import EventViewSet, AttendancesViewSet, SingleEventAttendance, EventAttendances

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('attendances', AttendancesViewSet, basename='attendances')

custom_urlpatterns = [
   url(r'events/(?P<event_pk>\d+)/attendances$', EventAttendances.as_view(), name='event_attendances'),
   url(r'events/(?P<event_pk>\d+)/attendances/(?P<pk>\d+)$', SingleEventAttendance.as_view(),
       name='single_category_recipe')
]
urlpatterns = router.urls
urlpatterns += custom_urlpatterns

# urlpatterns = [
#     path('', include(router.urls))
# ]