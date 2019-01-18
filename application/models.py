from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=200)
    remark = models.CharField(max_length=1000)
    status = models.IntegerField()
    warPath = models.CharField(max_length=1000)