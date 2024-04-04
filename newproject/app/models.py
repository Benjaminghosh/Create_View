from django.db import models

# Create your models here.

class School(models.Model):
    sname = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    contact = models.CharField(max_length=14)


class Student(models.Model):
    sname = models.CharField(max_length=50)
    stdname = models.CharField(max_length=50)
    stdage = models.CharField(max_length=50)

    