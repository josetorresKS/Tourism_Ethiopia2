from rest_framework import generics, filters
from .serializers import UserSerializer
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
  

class UserList(generics.ListAPIView):
    # Get all posts, limit = 20
    queryset = User.objects.order_by('created_at').reverse().all()[:20]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class UserAdd(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class UserDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]