from django.conf.urls import patterns, url

from lostpet import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'new/$', views.new, name='new'),
                       )
