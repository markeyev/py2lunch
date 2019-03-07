# coding: utf-8

from django.conf.urls import url

from restaurants.views import home_page, restaurants

urlpatterns = (
    url(r'^$', home_page, name='index'),
    url(r'^restaurants/$', restaurants, name='restaurants'),
)
