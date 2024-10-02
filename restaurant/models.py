from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)
   reservation_date = models.DateField(default=timezone.now)
   reservation_slot = models.TimeField(default=datetime.time(12, 0))

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   description = models.TextField(max_length=1000,default="No description")

   def __str__(self):
      return self.name

