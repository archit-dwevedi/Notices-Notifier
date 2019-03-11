from django.db import models

# Create your models here.





class telegram_id(models.Model):
    tel_id=models.IntegerField(unique=True)
    sub=models.BooleanField(default=False)


    def __str__(self):
        return str(self.tel_id)



class telegram_offset(models.Model):
    active=models.BooleanField(default=False)
    offset=models.IntegerField()


    def __str__(self):
        return str(self.offset)
