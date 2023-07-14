from django import forms 
from .models import Register
class Name(models.Model):
    name=models.CharField(max_length=200)