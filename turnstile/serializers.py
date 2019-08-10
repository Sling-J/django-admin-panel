from userAPI.models import UserProfile as User
from .models import Attendance, Turnstile
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError
)

class AttendanceCreateSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'user',
            'turnstile'
        ]
    def validate(self, data):
        user = data['user']
        turnstile = data['turnstile']
        user_qs = User.objects.filter(username=user)
        turnstile_qs = Turnstile.objects.filter(name=turnstile) 
        if user_qs.exists() and turnstile_qs.exists():
            v_user = User.objects.get(username=user)
            if v_user.is_active is True:
                return data
            else:
                raise ValidationError("An user is not active.")
        else:
            raise ValidationError("This user/turniket does not exists.")

class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'user',
            'turnstile',
            'time'
        ]
