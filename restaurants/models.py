# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rating = models.FloatField(default=0)

    raw_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Go(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=None)
    restaurant = models.ForeignKey('Restaurant', on_delete=None)

    def __str__(self):
        return '{} to {}'.format(self.user, self.restaurant)

    class Meta:
        unique_together = ('user', 'restaurant')
