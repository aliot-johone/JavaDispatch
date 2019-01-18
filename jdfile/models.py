from django.db import models

# Create your models here.

class JdFile(models.Model):
    path = models.CharField(max_length=1000)
    origin = models.CharField(max_length=1000)
    newName = models.CharField(max_length=1000)
    module = models.CharField(max_length=1000)
    moduleId = models.IntegerField()
    uploadTime=models.DateTimeField()
    status=models.IntegerField()
    