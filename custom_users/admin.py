# -*- coding: utf-8 -*-
from django.contrib.gis import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from custom_users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(admin.OSMGeoAdmin):
    filter_horizontal = ('interests',)
    
admin.site.register(CustomUser, CustomUserAdmin)