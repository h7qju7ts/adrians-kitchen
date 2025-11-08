from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.restaurant.name} on {self.date} at {self.time}"
