"""Pythonzhcn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .home import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^posted/$', views.posted),
    url(r'^posted/detils/$', views.posted_detils),
    
    url(r'^sigin/', views.sigin),
    url(r'^sigup/', views.sigup),
    
    url(r'^user/info/', views.user_info),
    url(r'^user/settings', views.user_settings),
    url(r'^user/message/', views.message),
]
