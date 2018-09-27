from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 50)


class Owner(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE )


class Task(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField('Created', '', auto_now_add=True)
    due_on = models.DateTimeField('Due on')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    done = models.NullBooleanField('Done')
