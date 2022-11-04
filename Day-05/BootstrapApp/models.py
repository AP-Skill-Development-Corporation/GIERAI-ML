from django.db import models

# Create your models here.

class Student(models.Model):
	stroll = models.CharField(max_length=50)
	stname = models.CharField(max_length=80)
	stbranch = models.CharField(max_length=20)
	styear = models.IntegerField()
