from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from ckeditor_uploader import views
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.conf.urls.static import static
from django.conf import settings
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'videos', views.VideoView, 'videos')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'),
    url(r'^ckeditor/browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
