from django.db import models
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
