from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer
from .models import User


# ..........register.........

class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# ..........login............

class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.none()
    permission_classes = [AllowAny]


# ..........log out.........


class LogoutViewSet(viewsets.ViewSet):
    def create(self, request):
        refresh_token = request.data.get('refresh_token')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'success': 'User successfully logged out.'})
            except Exception as e:
                return Response({'error': str(e)}, status=400)
        else:
            return Response({'error': 'Invalid request.'}, status=400)


