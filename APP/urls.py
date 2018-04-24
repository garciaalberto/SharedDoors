from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/validation/', views.validation_register, name='validation_register'),
    url(r'^login/validation/', views.validation_login, name='validation_login'),
    url(r'^flat/', views.flat, name='flat'),
    url(r'^flat-create', views.createflat, name='createflat'),
    url(r'^flat-create/validation', views.validation_createflat, name='validation_createflat'),
    url(r'^flat-join', views.joinflat, name='joinflat'),
    url(r'^flat-join/validation', views.validation_joinflat, name='validation_joinflat')
]

