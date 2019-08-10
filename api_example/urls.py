from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from absl import logging
# logging._warn_preinit_stderr = 0
# logging.warning('Worrying Stuff')

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('users/', include('userAPI.urls')),
    path('attendances/', include('turnstile.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='myAdmin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myAdmin/logout.html'), name='logout'),
    path('', include('myAdmin.urls')),
    # path('face/', include(('faceRec.urls')))
    # path('^api-auth/', include('rest_framework.urls'))

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
