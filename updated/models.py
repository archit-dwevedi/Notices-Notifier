from django.db import models

# Create your models here.



class update(models.Model):
	notice_id=models.DecimalField(default=0.00,max_digits=1000,decimal_places=1)
	notice=models.CharField(max_length=100,unique=True)
	

	def __str__(self):
		return self.notice