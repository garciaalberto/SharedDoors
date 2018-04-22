from django.shortcuts import render


def index(request):
    context = {
        'title': 'Identification'
    }
    return render(request, '../SharedDoors-templates/APP/index.html', context)
