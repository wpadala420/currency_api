from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

class CurrencySubscription(models.Model):
    subscribent = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    currency_name = models.CharField(max_length=20)

# Create your models here.
