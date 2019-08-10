from django.shortcuts import render
from django.http import HttpResponse
from userAPI.models import UserProfile as User
from userAPI.admin import UserProfileAdmin
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from turnstile.models import Attendance
from django.contrib.auth.forms import UserCreationForm


@login_required
def base_admin(request):
  return render(request, 'myAdmin/base_admin.html')

@login_required
def index(request):
  users = User.objects.all()
  search_fields = UserProfileAdmin.search_fields
  user = request.GET.get('q')
  if user:
    users = users.filter(
      Q(username__icontains=user)|
      Q(first_name__icontains=user)|
      Q(last_name__icontains=user)|
      Q(email__icontains=user)
    ).distinct()
  context={'users':users, 'fields':search_fields}
  return render(request, 'myAdmin/index.html', context)


@login_required
def attendance(request):
  attendances = Attendance.objects.all()
  context = {'attendances':attendances}
  return render(request, 'myAdmin/attendance.html', context)
# Create your views here.

def register(request):
  form = UserCreationForm()
  return render(request, 'myAdmin/register.html', {'form':form})
# def   