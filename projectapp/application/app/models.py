from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', related_name='following', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)
    profile_image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    theme = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.theme}'


class Video(models.Model):
    video = RichTextUploadingField(default='')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='VideoCategory')
    rate_video = models.IntegerField(default=0, null=True)

    def like(self):
        self.rate_video = self.rate_video + 1
        self.save()

    def dislike(self):
        self.rate_video -= Video.objects.get(id=1).rate_video
        self.save()

class Comments(models.Model):
    author = models.ManyToManyField(UserProfile)
    text = models.CharField(max_length=2048)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)

class VideoCategory(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)


class Room(models.Model):
    room_name = models.TextField(verbose_name='Название комнаты')
    participants = models.ManyToManyField(User, blank=True, null=True)

    def get_absolute_url(self):
        return f'/{self.id}'


class Room_message(models.Model):
    send = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    text = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
