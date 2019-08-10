from django.urls import path
from faceRec import views as app_views

urlpatterns = [
    path('', app_views.faceRecog)
]
