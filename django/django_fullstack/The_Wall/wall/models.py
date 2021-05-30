from django.db import models
from reglog.models import user

class Post(models.Model):
    user_id = models.ForeignKey(user, related_name="posts", on_delete = models.CASCADE)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user_id = models.ForeignKey(user, related_name="comments", on_delete = models.CASCADE)
    post_id = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
