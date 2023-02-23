from rest_framework import viewsets, mixins
from .serializers import RegisterSerializer
from .models import User


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


