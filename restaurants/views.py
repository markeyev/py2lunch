# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from restaurants.models import Restaurant

@login_required
def home_page(request):
    return render(request, 'index.html')


@login_required
def restaurants(request):
    return JsonResponse({
        'restaurants': [{
            'id': r.pk,
            'name': r.name,
            'rating': r.rating,
        } for r in Restaurant.objects.all()],
        'voted': False or True,
    })
