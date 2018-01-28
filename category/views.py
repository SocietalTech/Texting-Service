# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from twilio.twiml import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.views.generic.edit import CreateView
from .models import Attribute, Category

class AttributeCreate(CreateView):
    model = Attribute
    fields = '__all__'

attribute_create = AttributeCreate.as_view()

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'

category_create = CategoryCreate.as_view()

 
@twilio_view
def sms(request):
    category_name = request.POST.get('Body', '')
    category_obj = Category.objects.filter(name=category_name).first()
    msg = ''
    if category_obj:
        msg = '%s\n'%category_obj.url

        attributes = category_obj.attribute_set.all().order_by('name')
        for attribute_obj in attributes:
            msg += '%s,%s,%s\n' %(attribute_obj.name,attribute_obj.address,attribute_obj.phone_number)
    else:
        msg = 'Sorry, I don\'t understand your text. Please text me one of the following: Shelters, Showers, Food, Clothing'

    r = Response()
    r.message(msg)
    return r
