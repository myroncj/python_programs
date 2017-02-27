from django.db import models

# Create your models here.

class student(models.Model):
        name=models.CharField(max_length=20)
        branch=models.CharField(max_length=20)
        age=models.IntegerField()
        
class users(models.Model):
        u_name=models.CharField(max_length=20)
        p_word=models.CharField(max_length=20)
