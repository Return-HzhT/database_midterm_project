from django.db import models
from django.db import transaction

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=64)

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    views = models.PositiveIntegerField(default=0)
    favorites = models.PositiveIntegerField(default=0)
    comments= models.PositiveIntegerField(default=0)

    @transaction.atomic
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    @transaction.atomic
    def increase_comments(self):
        self.comments += 1
        self.save(update_fields=['comments'])

    @transaction.atomic
    def increase_favorites(self):
        self.favorites += 1
        self.save(update_fields=['favorites'])

    @transaction.atomic
    def decrease_favorites(self):
        self.favorites -= 1
        if self.favorites<0:
            self.favorites=0
        self.save(update_fields=['favorites'])

class Comment(models.Model):
    speaker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_index=True)
    body = models.TextField()
    now_floor = models.PositiveIntegerField(default=0)
    to_floor = models.PositiveIntegerField(default=0)

class Follow(models.Model):
    follower_user = models.PositiveIntegerField(default=0, db_index=True)
    followed_user = models.PositiveIntegerField(default=0)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
