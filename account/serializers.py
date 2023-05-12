
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User

# ..............register serializer..............


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# ..............login serializer..............


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()

    def get_access_token(self, obj):
        return str(obj['access_token'])

    def get_refresh_token(self, obj):
        return str(obj['refresh_token'])

    def create(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            raise serializers.ValidationError('Please enter both username and password.')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Incorrect credentials.')

        if not user.is_active:
            raise serializers.ValidationError('Inactive user.')

        refresh = RefreshToken.for_user(user)

        return {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'access_token': refresh.access_token,
            'refresh_token': refresh,
        }
