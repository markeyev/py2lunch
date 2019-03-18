# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from restaurants.models import Restaurant, Go


@admin.register(Restaurant)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating')
    ordering = ('rating',)
    fields = ('name', 'address', 'raw_data')


admin.site.register(Go)
