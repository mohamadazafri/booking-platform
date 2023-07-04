from django.db import models

# Create your models here.

class Homestay(models.Model):
    name = models.CharField(null=False, blank=False)
    total_unit = models.IntegerField(null=False, default= 1)

class HouseUnit(models.Model):
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE)
    house_number = models.IntegerField(blank=True)
    bathroom = models.IntegerField(default=1)
    bedroom = models.IntegerField(default=1)
    necessity = models.JSONField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

class Customer(models.Model):
    name = models.CharField(blank=False, null=False)
    phone_number = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True ,null=True)
    origin = models.CharField(blank=True ,null=True)

class Invoice(models.Model):
    title = models.CharField()
    content = models.BinaryField(null=False, blank=False, default=None)
    receipt_number = models.IntegerField(unique=True)

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    house_unit = models.ForeignKey(HouseUnit, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    check_in_date = models.DateField(null=False, blank=False)
    check_in_time = models.TimeField(null=False, blank=False, default='15:00')
    check_out_date = models.DateField(null=False, blank=False)
    check_out_time = models.TimeField(null=False, blank=False, default='12:00')
    total_adult = models.IntegerField(blank=True)
    total_child = models.IntegerField(blank=True, null = True, default=0)
    purpose_of_booking = models.CharField(blank=True, null=True)
    confirmation_code = models.CharField(unique=True)




    





    




