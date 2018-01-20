# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Stock(models.Model):
    key = models.CharField(max_length=30)
    stock = models.IntegerField()
    location = models.CharField(max_length=1000)
