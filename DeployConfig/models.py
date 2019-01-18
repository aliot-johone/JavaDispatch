from django.db import models

# Create your models here.

class DeployConfig(models.Model):
    serverId = models.IntegerField()
    applicationId = models.IntegerField()
    remark = models.CharField(max_length=1000)
    status = models.IntegerField()
    configPath = models.CharField(max_length=1000)
    deployPath = models.CharField(max_length=2000)
    shell = models.CharField(max_length=2000)
    url = models.CharField(max_length=2000)
    deployAS = models.CharField(max_length=2000)
    successResponse = models.CharField(max_length=2000)