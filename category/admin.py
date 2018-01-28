# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User, Group

from django_twilio.models import Caller, Credential

from .models import Category, Attribute

# admin.site.register(Category)
# admin.site.register(Attribute)

class AttributeInline(admin.TabularInline):
    model = Attribute

class CategoryAdmin(admin.ModelAdmin):
    inlines = [AttributeInline,]

admin.site.register(Category,CategoryAdmin)

# unregister not required models
admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.unregister(Caller)
# admin.site.unregister(Credential)
