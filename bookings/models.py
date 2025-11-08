from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    """
       This model stores the information for each table booking:

       name, email, phone — who booked

       date, time, people — when and how many

       created_at — automatically added timestamp
     """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
