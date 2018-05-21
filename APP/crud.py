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


def get_user_by_id(user_id):
    return User.objects.get(id=user_id)


def get_user_by_mail(user_mail):
    return User.objects.get(mail=user_mail)


def get_session_user(request):
    return User.objects.get(id=request.session['user_id'])


def get_session_flat(request):
    return get_session_user(request).allocation


def get_all_flatmates(request):
    return User.objects.filter(allocation=Flat.objects.get(id=get_session_flat(request).id))


def get_all_events(request):
    return Event.objects.filter(users=get_session_user(request))


def get_event_by_id(event_id):
    return Event.objects.get(id=event_id)


def get_event_by_name(event_name):
    return Event.objects.get(name=event_name)


def get_flat_by_id(flat_id):
    return Flat.objects.get(id=flat_id)


def get_flat_by_key(key):
    return Flat.objects.get(key=key)


def delete_seesion_user(request):
    user = get_session_user(request)
    user.delete()


def leave_flat_session_user(request):
    user = get_session_user(request)
    user.points_total = 0
    user.points_monthly = 0
    for event in get_all_events(request):
        event.users.remove(user)
    user.allocation = None
    user.save()


def delete_event_by_id(event_id):
    event = get_event_by_id(event_id)
    event.delete()
