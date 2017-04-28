# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from models import RGSUser, Interest
from serializers import RGSUserSerializer

# Create your views here.
class RGSUserViewSet(viewsets.ModelViewSet):
	queryset = RGSUser.objects.all()
	serializer_class = RGSUserSerializer

	ENTRIES_PER_PAGE = 10

	@list_route(methods=['post'])
	def new_user(self, request):
		try:
			with transaction.atomic():
				name = request.POST['name']
				lastname = request.POST['lastname']
				gender = request.POST['gender']
				age = request.POST['age']
				interests = request.POST['interests'].split(',')

				u = RGSUser(name=name, lastname=lastname, gender=gender, age=age)
				u.save()
				for i in interests:
					interest = Interest.objects.get(id=int(i))
					u.interests.add(interest)
				u.save()
				return Response("User successfully added!")
		except ObjectDoesNotExist:
			return Response("Error: Interest does not exist.")
		except:
			return Response("Error: An error has occurred.")

	@list_route(methods=['get'])
	def filter_users(self, request):
		gender = request.GET['gender']
		age = request.GET['age']
		page = int(request.GET['page']) if 'page' in request.GET else 0

		start = self.ENTRIES_PER_PAGE*page
		end = self.ENTRIES_PER_PAGE*(page + 1)

		users = RGSUser.objects.filter(gender=gender, age=age)[start:end]

		return Response({'page': page, 'users': self.serializer_class(users, many=True).data})