# from django.urls import path, include
# from . import views
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('register', views.UserCreateAPIView)
#
# urlpatterns = [
#     path('', include(router.urls))
# ]

from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
)

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),


]
