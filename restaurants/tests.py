# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse


class RestaurantEndpointTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_endpoint_with_no_auth(self):
        response = self.client.get(path=reverse('restaurants'))
        self.assertEqual(response.status_code, 302)  # Because of redirect to login.

    def test_endpoint(self):
        # TODO: write me!
        response = self.client.get(path=reverse('restaurants'))
        # data = response.json()

        # self.assertDictEqual(data, )
