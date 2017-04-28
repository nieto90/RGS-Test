# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class RGSUser(models.Model):
	GENDER = (
		('M', 'Male'),
		('F', 'Female')
	)
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER)
	age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
	interests = models.ManyToManyField('Interest')

	def __str__(self):
		return str(self.name) + " " + str(self.lastname)

	class Meta:
		verbose_name = "RGS User"

class Interest(models.Model):
	desc = models.CharField(max_length=20)

	def __str__(self):
		return str(self.desc)

	class Meta:
		verbose_name = "Interest"