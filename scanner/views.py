# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def start_deposit(request):
    return render(request, 'deposit.html')


def start_collect(request):
    return render(request, 'collect.html')
