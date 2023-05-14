from django.db import models

# Create your models here.

class Homestay(models.Model):
    name = models.CharField(null=False)
    total_unit = models.IntegerField(null=False, default= 1)

class HouseUnit(models.Model):
    homestay_id = models.ForeignKey(Homestay, on_delete=models.CASCADE)
    house_number = models.IntegerField(blank=True)
    bathroom = models.IntegerField(default=1)
    bedroom = models.IntegerField(default=1)
    necessity = models.JSONField(blank=True)

class Customer(models.Model):
    name = models.CharField(blank=False, null=False)
    phone_number = models.CharField(blank=True)
    email = models.CharField(blank=True)
    origin = models.CharField(blank=True)

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(null=False, blank=False)
    check_out_date = models.DateTimeField(null=False, blank=False)
    total_adult = models.IntegerField(blank=True)
    total_child = models.IntegerField(blank=True, default=0)
    purpose_of_booking = models.CharField(blank=True)





    




