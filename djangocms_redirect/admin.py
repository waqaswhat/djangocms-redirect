# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from .models import Redirect


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    list_display = ('old_path', 'new_path', 'response_code')
    list_filter = ('site',)
    search_fields = ('old_path', 'new_path')
    radio_fields = {'site': admin.VERTICAL}
