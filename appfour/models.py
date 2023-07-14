from django.db import models


# Create your models here.
class M(models.Model):
    name = models.CharField(max_length=100)
    num = models.IntegerField()
