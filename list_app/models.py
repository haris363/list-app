



from django.db import models
from django.contrib import admin
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    