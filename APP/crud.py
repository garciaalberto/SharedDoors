from .models import *


def create_user(name, mail, password, total_points=0, monthly_points=0, allocation=None):
    new_user = User(mail=mail, name=name, password=password, points_total=total_points, points_monthly=monthly_points, allocation=allocation)
    new_user.save()
    return new_user


def create_new_event(request, name, day, price, type):
    new_event = Event(name=name, day=day, price=price, type=type[0], allocation=get_session_flat(request))
    new_event.save()
    new_event.users.add(get_session_user(request))
    new_event.save()
    return new_event


def get_user(mail):
    return User.objects.get(mail=mail)


def get_session_user(request):
    return User.objects.get(id=request.session['user_id'])


def get_session_flat(request):
    return get_session_user(request).allocation


def get_all_flatmates(request):
    return User.objects.filter(allocation=Flat.objects.get(id=get_session_flat(request).id))


def get_all_events(request):
    return Event.objects.filter(users=get_session_user(request))

