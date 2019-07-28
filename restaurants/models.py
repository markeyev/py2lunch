# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import models


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


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=None)
    restaurant = models.ForeignKey('Restaurant', on_delete=None)
    review_text = models.TextField(null=False, blank=False)

    def __str__(self):
        return '{} posted review for {}'.format(self.user, self.restaurant)
