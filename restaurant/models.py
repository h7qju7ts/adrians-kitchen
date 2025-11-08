from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Restaurant(models.Model):
    name = models.Charfield(max_length=200)
    adress = models.CharField(max_length=300, blank=True)
    description = models.TextField(blanl=True)

    def __str__(self):
        return self.name
    
    
