# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Stock
import json
from django.views.decorators.csrf import csrf_exempt
import difflib


def home(request):
    return render(request, 'home.html')


def start_deposit(request):
    return render(request, 'deposit.html')


def start_collect(request):
    return render(request, 'collect.html')


def start_confirmation_modal(request):
    return render(request, 'confirmationmodals.html')


def start_collect_mobile(request):
    return render(request, 'mobile.html')


@csrf_exempt
def get_collection(request):

    stocks = Stock.objects.all()
    list_stock = []

    for stock in stocks:
        stock_json = {"key": stock.key, "stock": stock.stock, "location": stock.location}
        list_stock.append(stock_json)

    response = HttpResponse(json.dumps(list_stock), content_type='application/json')
    response["access-control-allow-origin"] = True
    return response


@csrf_exempt
def post_collection(request):

    post = json.loads(request.body)
    #
    stock = Stock.objects.filter(key=post.get("key")).update(stock=post.get("stock"))
    return HttpResponse(json.dumps({"success": True}), content_type='application/json')


@csrf_exempt
def insert_stock(request):
    stock = Stock()

    post = json.loads(request.body)

    stock.key = post.get("key")
    stock.stock = post.get("stock")
    stock.location = post.get("location")

    stock.save()

    return HttpResponse(json.dumps({"success": True}), content_type='application/json')


@csrf_exempt
def search_collection(request):

    if request.method == 'OPTIONS':
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')

    post = json.loads(request.body)
    stocks = Stock.objects.all()

    list_key = []

    for stock in stocks:

        val = difflib.SequenceMatcher(None, stock.key, post.get("query").upper()).ratio()

        if val >= 0.4:
            list_key.append({"key": stock.key, "stock": stock.stock, "location": stock.location, "val": val})

    check = [x for x in list_key if x.get("val") == 1]

    if len(check) == 1:
        list_key = check

    return HttpResponse(json.dumps(list_key), content_type='application/json')
