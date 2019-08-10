from django.db import models
from django.contrib.auth.models import User

class Turnstile(models.Model):
    name = models.CharField(max_length=150)
    ip_camera = models.CharField(max_length=150)
    # attendance = models.ManyToManyField('Attendance', blank=True, related_name='turnstiles')
    # def __str__(self):
    #     return self.name

class Attendance(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)
    turnstile = models.CharField(max_length=100)
    # def __str__(self):
        # return self.time
    class Meta:
        ordering = ('time',)
