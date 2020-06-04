from django.db import models

class college(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
