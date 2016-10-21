from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_plan, name='add_plan'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^destination/(?P<trip_id>\d+)$', views.destination, name='destination'),
    url(r'^destination/join/(?P<trip_id>\d+)$', views.join, name='join')
]
