from django.contrib import admin
from .models import Turnstile, Attendance

class TurnstileAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_camera')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('time', 'user', 'turnstile')
    list_filter = ('time',)

admin.site.register(Turnstile, TurnstileAdmin)
admin.site.register(Attendance, AttendanceAdmin)
