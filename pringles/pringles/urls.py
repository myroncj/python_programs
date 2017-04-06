"""pringles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from chips.views import index,save,first,next1,inputs,graph1,graph2

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^input/',index),
    url(r'^save/',save),
    #url(r'^plot/',plot),
    url(r'^first',first),
    url(r'^next',next1),
    url(r'^input',inputs),    
    url(r'^graph1',graph1),
    url(r'^graph2',graph2),
    
]