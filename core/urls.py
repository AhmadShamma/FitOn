from djoser.views import UserViewSet,TokenCreateView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path, include
from rest_framework.routers import SimpleRouter,DefaultRouter
from .views import *

# Create a router and register our UserViewSet with a custom basename
router = DefaultRouter()
djoser_router = SimpleRouter()

djoser_router.register(r'login', UserViewSet, basename='login')

router.register('trainer',TrainerView,basename='trainer')
router.register('client',ClientView,basename='client')



urlpatterns = [
    path('',include(router.urls)),
    path('',include(djoser_router.urls)),
    path(r'create_token',TokenObtainPairView.as_view(),name='create_token'),
    path(r'refresh_token',TokenRefreshView.as_view(),name='refresh_token')

    
]
