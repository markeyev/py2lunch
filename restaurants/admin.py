# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from restaurants.models import Restaurant, Go, Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Restaurant)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating')
    ordering = ('rating',)
    fields = ('name', 'address', 'raw_data')

    inlines = [ReviewInline]


admin.site.register(Go)
