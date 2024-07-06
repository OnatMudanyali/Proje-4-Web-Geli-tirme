from re import M
from django.db import models


class Teacher(models.Model):
  maas = models.CharField(max_length=10)
  brans = models.CharField(max_length=50)
  adsoyad = models.CharField(max_length=255)
  telefon = models.CharField(max_length=11)




# Create your models here.
