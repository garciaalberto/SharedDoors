from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from .crud import *
import random
import string


def index(request):
    return render(request, '../SharedDoors-templates/APP/index.html', {'title': 'Welcome to Shared Doors'})


def login(request):
    try:
        form_user = get_user(request.POST['mail'])
        if form_user.password == request.POST['pass']:
            request.session['user_id'] = form_user.id
            if form_user.allocation is None:
                return HttpResponseRedirect('/app/flat/')
            else:
                return HttpResponseRedirect('/app/home/')
        else:
            raise KeyError
    except(KeyError, User.DoesNotExist):
        return render(request, '../SharedDoors-templates/APP/login.html', {
            'title': 'Log In',
        })


def register(request):
    user_name = request.POST.get('name', '')
    user_mail = request.POST.get('mail', '')
    user_pass = request.POST.get('pass', '')
    try:
        if user_mail != '':
            User.objects.get(mail=request)
    except(KeyError, User.DoesNotExist):
        new_user = create_user(user_name, user_mail, user_pass)
        request.session['user_id'] = new_user.id
        return HttpResponseRedirect('/app/flat/')
    return render(request, '../SharedDoors-templates/APP/register.html', {'title': 'Register'})


def validation_register(request):
    return None


def validation_login(request):
    return None


def validation_createflat(request):
    return None


def validation_joinflat(request):
    return None


def validation_event(request):
    return None


def flat(request):
    user = get_session_user(request)
    return render(request, '../SharedDoors-templates/APP/flat.html', {
        'title': 'Have flat?',
        'user_name': user.name
    })


def createflat(request):
    flat_name = request.POST.get('flat_name', '')
    flat_key = randomize_key()
    if len(flat_name) < 256 and flat_name != '':
        try:
            Flat.objects.get(key=flat_key)
        except(KeyError, Flat.DoesNotExist):
            new_flat = Flat(name=flat_name, key=flat_key)
            new_flat.save()
            user = User.objects.get(id=request.session['user_id'])
            user.allocation = Flat.objects.get(id=new_flat.id)
            user.save()
            return HttpResponseRedirect('/app/home/')
    return render(request, '../SharedDoors-templates/APP/createflat.html', {'title': 'Create flat'})


def joinflat(request):
    flat_key = request.POST.get('flat_key', '')
    if len(flat_key) < 16 and flat_key != '':
        try:
            flat = Flat.objects.get(key=flat_key)
            user = get_session_user(request)
            user.allocation = Flat.objects.get(id=flat.id)
            user.save()
            return HttpResponseRedirect('/app/home/')
        except(KeyError, Flat.DoesNotExist):
            pass
    return render(request, '../SharedDoors-templates/APP/joinflat.html', {'title': 'Join flat'})


def home(request):
    return render(request, '../SharedDoors-templates/APP/home.html', {'title': 'Home',
                                                                      'user_name': get_session_user(request).name,
                                                                      'flat_name': get_session_flat(request).name})


def score_monthly(request):
    user_list = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/scores.html', {'title': 'Score',
                                                                        'user_list': user_list,
                                                                        'monthly': True,
                                                                        'type': 'Monthly'})


def score_total(request):
    user_list = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/scores.html', {'title': 'Total Score',
                                                                        'user_list': user_list,
                                                                        'monthly': False,
                                                                        'type': 'Total'})


def calendar(request):
    events = get_all_events(request)
    users = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/calendar.html', {
        'title': 'Calendar',
        'events': events,
        'users': users
    })


def complete(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.is_completed = True
    users = event.users.all()
    for user in users:
        user.points_monthly += 100
        user.points_total += 100
        user.save()
    event.save()
    return HttpResponseRedirect('/app/calendar/')


def create_event(request):
    event_name = request.POST.get('name', '')
    event_day = request.POST.get('day', '')
    event_price = request.POST.get('price', '')
    event_type = request.POST.get('type', '')
    try:
        if event_name != '':
            Event.objects.get(name=event_name)
    except(KeyError, Event.DoesNotExist):
        create_new_event(request, event_name, event_day, event_price, event_type)
        return HttpResponseRedirect('/app/calendar/')
    users_flat = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/createevent.html', {
        'title': 'Create a new event',
        'users_flat': users_flat
    })


def randomize_key():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
