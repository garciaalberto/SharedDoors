from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=25)
    points_total = models.IntegerField()
    points_monthly = models.IntegerField()
    #allocation = models.ForeignKey(Flat, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + " " + self.id;