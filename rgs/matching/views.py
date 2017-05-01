# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import F, Count, Case, When, IntegerField, Sum
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from models import RGSUser, Interest
from serializers import RGSUserSerializer

# Create your views here.
class RGSUserViewSet(viewsets.ModelViewSet):
	queryset = RGSUser.objects.all()
	serializer_class = RGSUserSerializer

	ENTRIES_FOR_PAGE = 10

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

		users = RGSUser.objects.filter(gender=gender, age=age)

		return Response(self.serializer_class(users, many=True).data)

	@list_route(methods=['post'])
	def match(self, request):
		user_id = int(request.POST['user'])
		user = RGSUser.objects.get(id=user_id)

		# if page is not an argument, return page 0
		page = int(request.POST['page']) if 'page' in request.POST else 0
		start = page*self.ENTRIES_FOR_PAGE
		end = start + self.ENTRIES_FOR_PAGE

		gender = 'M' if user.gender == 'F' else 'F'
		age = user.age
		interests = user.interests.all()

		# age score = 100 - 10*(age difference)
		# interests score = number of coincidences
		# total score = age score + interests score

		users = RGSUser.objects.filter(gender=gender)\
		.annotate(age_score=Case(
			When(age__gt=age, then=100-10*(F('age')-age)),
			When(age__lt=age, then=100-10*(age-F('age'))), 
			default=100, output_field=IntegerField()))\
		.annotate(inter_score=Sum(Case(
			When(interests__id__in=interests, then=1),
			default=0, output_field=IntegerField())))\
		.annotate(score=F('age_score')+F('inter_score'))\
		.order_by('-score')\
		.values('id', 'name', 'lastname', 'age', 'score')[start:end]

		return Response({'page': page, 'matches': users})