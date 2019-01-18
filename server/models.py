from django.db import models

# Create your models here.

class Server(models.Model):
    name = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    remark = models.CharField(max_length=1000)
    status = models.IntegerField()