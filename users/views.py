from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserModelSerializer,UserDetailSerializer


class UserList(generics.ListAPIView):
    """
        Список всех User
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserDetail(generics.RetrieveAPIView):
    """
        Детальная информация User
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
