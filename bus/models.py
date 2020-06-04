from django.db import models

class bus(models.Model):
    bus_no=models.CharField(max_length=15)
    bus_stand_name=models.CharField(max_length=30)
    bus_service_years=models.CharField(max_length=3)
class routes(models.Model):
    start=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    changeover=models.CharField(max_length=30)
