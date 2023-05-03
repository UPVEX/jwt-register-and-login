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

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({'error': 'Invalid Credentials'}, status=400)
        token = RefreshToken.for_user(user)
        return Response({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })
