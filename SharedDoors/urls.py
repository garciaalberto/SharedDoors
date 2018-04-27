from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^dev/', admin.site.urls),
    url(r'^app/', include('APP.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('/app/'))
]
