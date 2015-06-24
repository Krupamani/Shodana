from django.conf.urls import patterns, url
from list import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))

