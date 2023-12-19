from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number_of_guests = models.SmallIntegerField(default=1)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return f'{self.first_name} for {self.number_of_guests} guests on {self.reservation_date} {self.reservation_slot}00'


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name