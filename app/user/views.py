from rest_framework import generics
from .serializers import UserSerialzer

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerialzer