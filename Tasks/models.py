from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    createdOn = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
