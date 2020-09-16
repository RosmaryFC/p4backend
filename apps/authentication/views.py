from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
# allow all users to see the view
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User


# Create your views here.
class RegistrationAPIView(APIView):
    # Allow any user to hit this endpoint
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get("email"),
                "username": request.data.get("username"),
                "password": request.data.get("password"),
                "first_name": request.data.get("first_name"),
                "last_name": request.data.get("last_name"),
                "is_admin": request.data.get("is_admin")
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
