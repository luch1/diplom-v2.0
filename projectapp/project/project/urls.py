from django.contrib import admin
from django.urls import path, include

from app import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'videos', views.VideoView, 'videos')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include(router.urls)),
]
