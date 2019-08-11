from django.urls import path
from faceRec import views as app_views

urlpatterns = [
    path('', app_views.show_result, name='face_recog_answer'),
]
