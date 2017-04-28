# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import RGSUser, Interest

# Register your models here.
@admin.register(RGSUser)
class RGSUserAdmin(admin.ModelAdmin):
	fields = ('name', 'lastname', 'gender', 'age', 'interests')

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
	fields = ('desc',)