from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
from .models import User


class RegisterViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LoginSerializer
