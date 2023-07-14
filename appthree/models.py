from django.db import models


# Create your models here.
class AppThree(models.Model):
    Name = models.CharField(max_length=200)
    SRN = models.CharField(max_length=200)
    College = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    AGE = models.CharField(max_length=200)


class PostAPI(models.Model):
    pk1 = models.CharField(max_length=200)
