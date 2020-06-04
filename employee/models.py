from django.db import models

class emp(models.Model):
    emp_id=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=50)
    father=models.CharField(max_length=50)
    mother=models.CharField(max_length=50)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    designation=models.CharField(max_length=10)
class assign(models.Model):
    date=models.DateField()
    start=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    driver=models.CharField(max_length=30)
    conductor=models.CharField(max_length=30)
    conductor_name=models.CharField(max_length=30)
    driver_name=models.CharField(max_length=30)
    bus_no=models.CharField(max_length=10,default='123')
    code=models.CharField(max_length=20,default='1')

