from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    of_user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=96)

    def __str__(self):
        return self.name

class Task(models.Model):
    of_list=models.ForeignKey(List, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    