from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=100)


# Create your models here.
