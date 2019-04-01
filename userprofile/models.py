from django.db import models

# Create your models here.

class profile(models.Model):


	username=models.EmailField(max_length=100)
	name=models.CharField(max_length=100)
	sid=models.CharField(max_length=1000)
	token=models.CharField(max_length=1000)
	mobile=models.CharField(max_length=10)
	premium=models.BooleanField(default=True)
	sent=models.DecimalField(default=0.00,max_digits=1000,decimal_places=1)


	

	def __str__(self):
		return self.name