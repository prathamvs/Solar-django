from django.db import models

# Create your models here.

class Image(models.Model):
    area = models.CharField(max_length=20)
    img =  models.ImageField(upload_to='pics')
    desc = models.TextField()
    
class Points(models.Model):
    uid = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    current = models.IntegerField()
    voltage = models.IntegerField()
    energy = models.IntegerField()
    
class Data:
    area:str
    DCvolt: float
    ACvolt:float
    DCcurrent:float
    ACcurrent:float
    DCPower:float
    ACpower:float
    energy:float
    current:float
    irradiance:float
