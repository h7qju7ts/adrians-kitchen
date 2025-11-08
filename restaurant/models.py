from django.db import models
from django.contrib.auth.models import User

# Create your models here.

User = settings.AUTH_USER_MODEL

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

