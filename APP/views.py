from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

user = None
flat = None


def index(request):
    return render(request, '../SharedDoors-templates/APP/index.html', {'title': 'Welcome to Shared Doors'})


def login(request):
    try:
        form_user = User.objects.get(mail=request.POST['mail'])
        if form_user.password == request.POST['pass']:
            global user
            user = form_user
            if form_user.allocation is None:
                return HttpResponseRedirect('/app/flat/')
            else:
                global flat
                flat = user.allocation
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
    user_pass2 = request.POST.get('pass', '')
    if len(user_name) < 255 and len(user_mail) < 255 and len(user_pass) < 255 and user_pass == user_pass2 and user_name\
            != '' and user_mail != '' and user_pass != '':
        try:
            User.objects.get(mail=request)
        except(KeyError, User.DoesNotExist):
            new_user = User(mail=user_mail, name=user_name, password=user_pass, points_total=0, points_monthly=0)
            global user
            user = new_user
            new_user.save()
            return HttpResponseRedirect('/app/flat/')
    return render(request, '../SharedDoors-templates/APP/register.html', {'title': 'Register'})


def validation_register(request):
    return None


def validation_login(request):
    return None


def flat(request):
    global user
    name = user.name
    return render(request, '../SharedDoors-templates/APP/flat.html', {
        'title': 'Have flat?',
        'user_name': name
    })


def createflat(request):
    return None