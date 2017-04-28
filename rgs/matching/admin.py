# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import RGS_User, Interest

# Register your models here.
@admin.register(RGS_User)
class RGS_UserAdmin(admin.ModelAdmin):
	fields = ('name', 'lastname', 'gender', 'age', 'interests')

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
	fields = ('desc',)