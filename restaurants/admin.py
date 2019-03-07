# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from restaurants.models import Restaurant, Go

admin.site.register(Restaurant)
admin.site.register(Go)
