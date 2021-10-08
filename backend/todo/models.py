from django.db import models
from django.db.models.base import Model

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)

    def _str(self):
        return self.title
