from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/validation/', views.validation_register, name='validation_register'),
    url(r'^login/validation/', views.validation_login, name='validation_login'),
    url(r'^flat/', views.flat, name='flat'),
    url(r'^flat-create/', views.createflat, name='createflat'),
    url(r'^flat-create/validation/', views.validation_createflat, name='validation_createflat'),
    url(r'^flat-join', views.joinflat, name='joinflat'),
    url(r'^flat-join/validation/', views.validation_joinflat, name='validation_joinflat'),
    url(r'^home/', views.home, name='home'),
    url(r'^score/', views.score, name='score'),
    url(r'^calendar/', views.calendar, name='calendar'),
    path('complete/<int:event_id>/', views.complete, name='complete'),
    url(r'^create-event', views.create_event, name='create_event'),
    url(r'^create-event/validation', views.validation_event, name='validation_event'),
    path('display_event/<int:event_id>', views.display_event, name='display_event'),
    path('edit_event/<int:event_id>', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
    path('add_participant/<int:event_id>/<int:user_id>', views.add_participant, name='add_participant'),
    path('delete_participant/<int:event_id>/<int:user_id>', views.delete_participant, name='delete_participant'),
    url(r'^leave-flat/', views.leave_flat, name='leave_flat'),
    url(r'^delete-account/', views.delete_account, name='delete_account')
]
