from django.db import models

class Student1(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField()
