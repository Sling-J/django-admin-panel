from django.shortcuts import render
from django.http import HttpResponse
from userAPI.models import UserProfile as User
from userAPI.admin import UserProfileAdmin
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  users = User.objects.all()
  search_fields = UserProfileAdmin.search_fields
  bla = "USERLAR"
  
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
# Create your views here.

# def   