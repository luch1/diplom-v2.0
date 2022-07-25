from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('videos/$', views.VideoList.as_view(), name='videos'),
    path(r'^videos/(?P<pk>\d+)$', views.VideoDetail.as_view(), name='video-detail'),
    path(r'^webpush/', include('webpush.urls')),
    path('', views.index, name='index'),
    path('chat', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    path('api/users', views.user_list, name='user-list'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('<int:pk>', views.about_view, name='about'),
    path('register', views.register_view, name='register'),
    path('chat/create', views.roomcreate_view, name='room_create'),
    path('api/rooms/', views.room_list, name='roomlist'),
    path('chat/rooms/', views.rooms_view, name='room-list'),
    path('chat/rooms/<int:pk>', views.room, name='room_detail'),
    path('chat/rooms/subscribe/<int:pk>', views.subscribe_me),
    path('chat/rooms/unsubscribe/<int:pk>', views.unsubscribe_me),
]
urlpatterns = format_suffix_patterns(urlpatterns)
