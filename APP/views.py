from django.shortcuts import render

user = None
flat = None


def index(request):
    context = {
        'title': 'Welcome to Shared Doors'
    }
    return render(request, '../SharedDoors-templates/APP/index.html', context)


def login(request):
    context = {
        'title': 'Log In'
    }
    return render(request, '../SharedDoors-templates/APP/login.html', context)


def register(request):
    context = {
        'title': 'Register'
    }
    return render(request, '../SharedDoors-templates/APP/register.html', context)