from django.db import models
from django.utils import timezone

CATEGORY = (('感想', '感想'),('宣伝','宣伝'))

class Post(models.Model):
    title = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    create_time = models.DateTimeField(default=timezone.now)
    link = models.URLField()
    category = models.CharField(max_length=100, choices= CATEGORY)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
