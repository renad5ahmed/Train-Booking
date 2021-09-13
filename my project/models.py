from django.db import models

class User(models.Model):#hena de el database details
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    is_admin = models.BooleanField(default=False)

class Train(models.Model):
    trainID = models.CharField(max_length =50)
    trainColor = models.CharField(max_length =50)
    maxTripTime = models.IntegerField(default=3)

class Trip(models.Model):
    tripID = models.CharField(max_length =50)
    source = models.CharField(max_length =50)
    tripTime = models.IntegerField(default=1)
    destination = models.CharField(max_length =50)
    requiredNumberOfSeats = models.IntegerField(default=20)
    availableNumberOfSeats = models.IntegerField(default=0)
    trainID = models.CharField(max_length =50)
    cost = models.FloatField(default=0)
    Date = models.CharField(max_length =50)
    time = models.CharField(max_length =50)
    

