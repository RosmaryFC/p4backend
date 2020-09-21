from django.conf.urls import url
from apps.authentication.views import RegistrationAPIView, LoginAPIView, UserViewSet

urlpatterns = [
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
    url(r'^users/$', UserViewSet.as_view({'get': 'list'}), name='users')

]
