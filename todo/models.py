from django.db import models
from django.utils import timezone
# Create your models here.

class ToDo (models.Model):
    title = models.CharField(max_length=150)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title