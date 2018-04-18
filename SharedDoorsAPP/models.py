from django.db import models

# Create your models here.
class Flat(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(max_length=20)

class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=25)
    points_total = models.IntegerField()
    points_mensual = models.IntegerField()
    allocation = models.ForeignKey(Flat, null=True, on_delete=models.SET_NULL)

class Event(models.Model):
    day = models.DateField()
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True)
    allocation = models.ForeignKey(Flat, on_delete=models.CASCADE)

class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Event, on_delete=models.CASCADE)

