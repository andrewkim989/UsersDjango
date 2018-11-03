from django.conf.urls import url
from . import views   

urlpatterns = [
    url(r'^$', views.users),
    url(r'^users$', views.users),
    url(r'^users/new/$', views.add),
    url(r'^users/create$', views.add_process),
    url(r'^users/(?P<num>\d+)$', views.show),
    url(r'^users/(?P<num>\d+)/edit$', views.edit),
    url(r'^users/(?P<num>\d+)/edit_process$', views.edit_process),
    url(r'^users/(?P<num>\d+)/delete$', views.delete),
]