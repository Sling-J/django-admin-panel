from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class UserProfile(AbstractUser):
    avatar  = models.ImageField(upload_to='avatar', blank=True)

    # def __str__(self):
    #     return self.user.username

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
    