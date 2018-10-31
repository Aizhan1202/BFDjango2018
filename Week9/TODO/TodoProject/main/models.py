from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 50)


class Owner(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE )

class DateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('created')

class Task(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField('Created', '', auto_now_add=True)
    due_on = models.DateTimeField('Due on')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    done = models.NullBooleanField('Done')
    created_objects = DateManager()
    objects = models.Manager()
