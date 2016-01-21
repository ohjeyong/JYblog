from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    text = models.TextField(max_length=500, blank=True)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=10)
    message = models.TextField(max_length=200)
    create_time = models.DateTimeField(auto_now=True)
