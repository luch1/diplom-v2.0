from .models import Message, Room
from rest_framework import serializers
from django.contrib.auth.models import User


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Video
       fields = ['id', 'name', 'text']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'room_name']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
