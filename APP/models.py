from django.db import models


class Flat(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(max_length=20)


class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=25)
    points_total = models.IntegerField()
    points_monthly = models.IntegerField()
    allocation = models.ForeignKey(Flat, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + " " + str(self.id)


class Event(models.Model):
    day = models.DateField()
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True)
    allocation = models.ForeignKey(Flat, on_delete=models.CASCADE)
    type = (
        ('M', 'Menu'),
        ('T', 'Task'),
        ('P', 'Payment'),
    )
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
