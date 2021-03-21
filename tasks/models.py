from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=255, default="Your TODO Here..", blank=False)
    task_description = models.TextField( blank=True, default="Your Todo Details")
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.task_title