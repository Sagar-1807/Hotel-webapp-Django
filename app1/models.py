from django.db import models
from django.db.models.fields import CharField
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.TextField(max_length=50)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=15)
    desc=models.TextField()
    date=models.DateField()
      
