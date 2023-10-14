from django.db import models

# Create your models here.
class product(models.Model):
    pname=models.CharField(max_length=50)
    pprice=models.IntegerField()

def __str__(self):
    self.pname +'' + self.pprice