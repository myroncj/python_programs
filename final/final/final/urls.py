"""final URL Configuration

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
from app1.views import index,save1,save2,save3,display,write

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index',index),
    url(r'^save1',save1),
    url(r'^save2',save2),
    url(r'^save3',save3),
    url(r'^display',display),
    url(r'^write',write),
]
