from django.db import models
from django.utils import timezone

# Create your models here.

class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author=1)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    author_objects = AuthorManager()
    objects = models.Manager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title