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
    path('attendances/', views.attendance, name='attendance'),
    path('user/<str:id>', views.user_detail, name='user_detail'),
]
