# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "vpn/home.html", {})

def about(request):
    return render(request, "vpn/home.html", {})

def contact(request):
    return render(request, "vpn/home.html", {})

def reach(request):
    return render(request, "vpn/home.html", {})

def functionaries(request):
    return render(request, "vpn/home.html", {})

def director(request):
    return render(request, "vpn/home.html", {})

def office(request):
    return render(request, "vpn/home.html", {})

def placement(request):
    return render(request, "vpn/home.html", {})

def record(request):
    return render(request, "vpn/home.html", {})

def recruiters(request):
    return render(request, "vpn/home.html", {})

def internship(request):
    return render(request, "vpn/home.html", {})

def opportunities(request):
    return render(request, "vpn/home.html", {})