from django.conf.urls import url
from django.contrib import admin

from .views import (
    AttendanceCreateAPIView,
    AttendanceListAPIView
)

urlpatterns = [
    url(r'^$', AttendanceListAPIView.as_view(), name='attendance'),
    url(r'^create/$', AttendanceCreateAPIView.as_view(), name='create'),


]
