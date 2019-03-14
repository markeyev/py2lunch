# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render


@login_required
def home_page(request):
    return render(request, 'index.html')


@login_required
def restaurants(request):
    return JsonResponse({
        'restaurants': [{
            'id': 1,
            'name': "Кокошка",
            'rating': 1,
        }, {
            'id': 2,
            'name': "Хуторок",
            'rating': 4,
        }, {
            'id': 3,
            'name': "Славковская",
            'rating': 2,
        }, {
            'id': 4,
            'name': "Пирогарня",
            'rating': 6,
        }, {
            'id': 5,
            'name': "Макдональлдс",
            'rating': 1,
        }],
        'voted': False or True,
    })
