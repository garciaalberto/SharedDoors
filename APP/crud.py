from .models import *


def create_user(name, mail, password, total_points=0, monthly_points=0, allocation=None):
    new_user = User(mail=mail, name=name, password=password, points_total=total_points, points_monthly=monthly_points, allocation=allocation)
    new_user.save()
    return new_user

