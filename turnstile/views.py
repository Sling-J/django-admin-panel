from django.shortcuts import render
from faceRec.views import faceRecog
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)
from rest_framework.response import Response
from .models import Attendance
from .serializers import (
    AttendanceCreateSerializer,
    AttendanceSerializer,
)


class AttendanceCreateAPIView(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceCreateSerializer

    def perform_create(self, serializer_class):
        serializer_class.save()
        print(serializer_class.data)
        faceRecog(self, serializer_class.data['user'], serializer_class.data['turnstile'])

class AttendanceListAPIView(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


