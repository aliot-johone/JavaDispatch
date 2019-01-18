from django.db import models

# account.py


class Account(models.Model):
    account = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
