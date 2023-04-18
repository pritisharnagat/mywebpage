from django.db import models

# Create your models here.
class English(models.Model):
    firstname=models.CharField(max_length=101)
    lastname=models.CharField(max_length=101)
    