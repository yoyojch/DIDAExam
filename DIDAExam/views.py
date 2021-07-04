from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.urls import reverse
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.conf.urls import url

import requests
import json
from datetime import datetime


def homeform(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')

def detailform(request):
     
    return render(request,'detail.html')

def detailform2(request):

    citizen=request.POST['citizen']
    name=request.POST['name']
    phone=request.POST['phone']

    province_from=request.POST['province_from']
    districts_from=request.POST['districts_from']
    subdistrict_from=request.POST['subdistrict_from']
    province_to=request.POST['province_to']
    districts_to=request.POST['districts_to']
    subdistrict_to=request.POST['subdistrict_to']      

    return render(request,'detail2.html',
    {

        'citizen':citizen,
        'name':name,
        'phone':phone,
        'province_from':province_from,
        'districts_from':districts_from,
        'subdistrict_from':subdistrict_from,
        'province_to':province_to,
        'districts_to':districts_to,
        'subdistrict_to':subdistrict_to

    })
