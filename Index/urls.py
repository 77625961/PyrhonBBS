# coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/(?P<pid>\d*)/', views.index, name='index'),
    url(r'^posted/$', views.posted, name='posted'),
    url(r'^posted/detils/$', views.posted_detils, name='reply'),
    
    url(r'^sigin/$', views.sigin, name='sigin'),
    url(r'^sigup/$', views.sigup, name='sigup'),
    
    url(r'^user/info/$', views.user_info),
    url(r'^user/settings/$', views.user_settings),
    url(r'^user/message/$', views.message),
]
