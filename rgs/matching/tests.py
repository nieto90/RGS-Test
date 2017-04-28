# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from views import RGSUserViewSet

# Create your tests here.
class RGSUserViewTests(TestCase):

	def test_new_user(self):
		factory = APIRequestFactory()
		request = factory.post('/new_user/', {'name': 'Test', 'lastname': 'LastTest', 'gender': 'M', 'age': 29, 'interests': ''})
		view = RGSUserViewSet.as_view({'post':'list'})
		response = view(request)
		response.render()
		self.assertEqual(response.status_code, 200)