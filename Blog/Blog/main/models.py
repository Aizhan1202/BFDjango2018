from django.db import models

# Create your models here.

class Post:
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created = models.DateTimeField('Created', '', auto_now_add=True)

class Comment:
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
