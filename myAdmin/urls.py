from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from myAdmin import views
# from .views import (
#     AttendanceCreateAPIView,
#     AttendanceListAPIView
# )

urlpatterns = [
    path('', views.base_admin, name='base_admin'),
    path('users/', views.index, name='index'),
    path('turnstile/', views.turnstile, name='turnstile'),
    path('skip-user/', views.skipUser, name='skip-user'),
    path('attendances/', views.attendance, name='attendance'),
    path('user/<str:pk>', views.user_detail, name='user_detail'),
]
