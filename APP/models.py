from django.db import models


class Flat(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.EmailField()
    points_total = models.IntegerField()
    points_monthly = models.IntegerField()
    allocation = models.ForeignKey(Flat, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Event(models.Model):
    day = models.DateField()
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    allocation = models.ForeignKey(Flat, on_delete=models.CASCADE)
    type = (
        ('M', 'Menu'),
        ('T', 'Task'),
        ('P', 'Payment'),
        ('B', 'Birthday')
    )
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
