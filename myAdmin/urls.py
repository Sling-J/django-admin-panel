from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from myAdmin import views
# from .views import (
#     AttendanceCreateAPIView,
#     AttendanceListAPIView
# )

urlpatterns = [
    path('admin/', views.index, name='index'),

]
