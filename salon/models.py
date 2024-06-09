from django.db import models

class Booking(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Product_Nmae = models.CharField(max_length=255)
    resrv_Date = models.CharField(max_length=255)
    pay_method = models.CharField(max_length=8)

    class Meta:
        db_table = "reservation"
