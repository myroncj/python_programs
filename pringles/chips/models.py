from django.db import models

# Create your models here.    
class chips1(models.Model):
    t=models.IntegerField()
    s=models.IntegerField()
    
class gps(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()