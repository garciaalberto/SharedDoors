from django.db import models


TYPES = (
        ('M', 'Menu'),
        ('T', 'Task'),
        ('P', 'Payment'),
        ('B', 'Birthday')
        )


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
    is_completed = models.BooleanField(default=False)
    day = models.DateField()
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True)
    allocation = models.ForeignKey(Flat, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPES)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
