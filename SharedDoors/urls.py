from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dev/', admin.site.urls),
    url(r'^user/', include('User.urls')),
]
