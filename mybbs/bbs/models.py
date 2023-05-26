from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=64)

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    views = models.PositiveIntegerField(default=0)
    favorites = models.PositiveIntegerField(default=0)
    comment_sum = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def increase_favorites(self):
        self.favorites += 1
        self.save(update_fields=['favorites'])

class Comment(models.Model):
    speaker = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    floor = models.IntegerField(default=0)

class Follow(models.Model):
    follower_user = models.PositiveIntegerField()
    followed_user = models.PositiveIntegerField()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
