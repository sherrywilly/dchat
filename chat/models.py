from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(
        User, related_name="author_messages", on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        _x = Message.objects.order_by('-timestamp').all()[:10]
        return _x[::-1]
