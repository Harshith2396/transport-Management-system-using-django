from django.db import models

class studs(models.Model):
    usn=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=50)
    father=models.CharField(max_length=50)
    mother=models.CharField(max_length=50)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=6)
    college=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    start=models.CharField(max_length=50)
    destiantion=models.CharField(max_length=50)
    changeover=models.CharField(max_length=50)
    ackno=models.CharField(max_length=10,default='nill')
    status=models.CharField(max_length=15,default='not approved')
    email=models.EmailField(max_length=100,default='NA')
    phone=models.CharField(max_length=10,default='NA')
    statusc=models.CharField(max_length=10,default='No')
