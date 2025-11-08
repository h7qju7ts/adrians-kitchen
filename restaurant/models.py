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
    

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.restaurant.name} review by {self.user}"