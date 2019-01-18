from django.db import models

# Create your models here.
class Task(models.Model):
    serverId = models.IntegerField()
    applicationId = models.IntegerField()
    dcId = models.IntegerField()
    host=models.CharField(max_length=1000)
    warPath=models.CharField(max_length=1000)
    deployAS=models.CharField(max_length=1000)
    md5val=models.CharField(max_length=1000)
    remark = models.CharField(max_length=1000)
    deployPath = models.CharField(max_length=2000)
    shell = models.CharField(max_length=2000)
    status = models.IntegerField()
    createTime=models.DateTimeField()