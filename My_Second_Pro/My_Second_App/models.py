from django.db import models

# Create your models here.

class Emp(model.Model):
  eno = models.IntegerField()

  ename = models.CharField(max_length=100)
