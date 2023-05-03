from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewset, LoginViewset


router = DefaultRouter()
router.register(r'register', RegisterViewset, basename='register')
router.register(r'login', LoginViewset, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]