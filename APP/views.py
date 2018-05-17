from django.shortcuts import render
from django.http import HttpResponseRedirect
from .crud import *
import random
import string
import clipboard
import datetime

def index(request):
    return render(request, '../SharedDoors-templates/APP/index.html', {'title': 'Welcome to Shared Doors'})


def login(request):
    try:
        form_user = get_user_by_mail(request.POST['mail'])
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
            get_user_by_mail(user_mail)
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
            get_flat_by_key(flat_key)
        except(KeyError, Flat.DoesNotExist):
            new_flat = Flat(name=flat_name, key=flat_key)
            new_flat.save()
            user = get_user_by_id(request.session['user_id'])
            user.allocation = get_flat_by_id(new_flat.id)
            user.save()
            return HttpResponseRedirect('/app/home/')
    return render(request, '../SharedDoors-templates/APP/createflat.html', {'title': 'Create flat'})


def joinflat(request):
    flat_key = request.POST.get('flat_key', '')
    if len(flat_key) < 16 and flat_key != '':
        try:
            flat = get_flat_by_key(flat_key)
            user = get_session_user(request)
            user.allocation = get_flat_by_id(flat.id)
            user.save()
            return HttpResponseRedirect('/app/home/')
        except(KeyError, Flat.DoesNotExist):
            pass
    return render(request, '../SharedDoors-templates/APP/joinflat.html', {'title': 'Join flat'})


def home(request):
    flat = get_session_flat(request)
    user = get_session_user(request)
    return render(request, '../SharedDoors-templates/APP/home.html', {
                                                                      'title': 'Home',
                                                                      'user': user,
                                                                      'flat': flat
                                                                      })


def score_monthly(request):
    user_list = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/scores.html', {
                                                                        'title': 'Score',
                                                                        'user_list': user_list,
                                                                        'monthly': True,
                                                                        'type': 'Monthly'
                                                                        })


def score_total(request):
    user_list = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/scores.html', {
                                                                        'title': 'Total Score',
                                                                        'user_list': user_list,
                                                                        'monthly': False,
                                                                        'type': 'Total'
                                                                        })


def calendar(request):
    return render(request, '../SharedDoors-templates/APP/calendar.html', {
                                                                          'title': 'Calendar',
                                                                          'events': get_all_events(request),
                                                                          'today': datetime.datetime.today().date(),
                                                                          'flat_key': get_session_flat(request).key
                                                                          })


def complete(request, event_id):
    event = get_event_by_id(event_id)
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
            get_event_by_name(event_name)
    except(KeyError, Event.DoesNotExist):
        create_new_event(request, event_name, event_day, event_price, event_type)
        return HttpResponseRedirect('/app/calendar/')
    return render(request, '../SharedDoors-templates/APP/createevent.html', {'title': 'Create a new event'})


def display_event(request, event_id):
    event = get_event_by_id(event_id)
    users = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/displayevent.html', {
                                                                              'title': event.name,
                                                                              'event': event,
                                                                              'users': users,
                                                                              })


def delete_event(request, event_id):
    delete_event(event_id)
    return HttpResponseRedirect('/app/calendar/')


def delete_participant(request, event_id, user_id):
    event = get_event_by_id(event_id)
    user = get_user_by_id(user_id)
    event.users.remove(user)
    event.save()
    users = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/displayevent.html', {
                                                                              'title': event.name,
                                                                              'event': event,
                                                                              'users': users
                                                                              })


def add_participant(request, event_id, user_id):
    event = get_event_by_id(event_id)
    user = get_user_by_id(user_id)
    event.users.add(user)
    event.save()
    users = get_all_flatmates(request)
    return render(request, '../SharedDoors-templates/APP/displayevent.html', {
                                                                              'title': event.name,
                                                                              'event': event,
                                                                              'users': users
                                                                              })


def delete_account(request):
    delete_seesion_user(request)
    return HttpResponseRedirect('/app/')


def leave_flat(request):
    leave_flat_session_user(request)
    return HttpResponseRedirect('/app/flat/')


def get_key(request):
    flat = get_session_flat(request)
    clipboard.copy(flat.key)
    return HttpResponseRedirect('/app/home/')


def randomize_key():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
