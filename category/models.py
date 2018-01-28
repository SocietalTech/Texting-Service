# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Attribute(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    # phone_number = models.CharField(max_length=12)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
