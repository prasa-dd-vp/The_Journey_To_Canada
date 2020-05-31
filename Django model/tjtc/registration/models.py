from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Meta:
    db_table = "user"