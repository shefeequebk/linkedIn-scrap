from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
# from views import PostView
from rest_framework.authtoken.views import obtain_auth_token

from core.views import PostView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('scrap-connections/', PostView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
