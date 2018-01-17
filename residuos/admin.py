# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Residuo
from django.contrib import admin

class ResiduoAdmin(admin.ModelAdmin):

    list_display = ['name', 'codigo', 'created_at']
    search_fields = ['name', 'codigo']

admin.site.register(Residuo, ResiduoAdmin)
