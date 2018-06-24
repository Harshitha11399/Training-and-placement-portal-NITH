# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "vpn/home.html", {})

def about(request):
    return render(request, "vpn/about.html", {})

def contact(request):
    return render(request, "vpn/contact.html", {})

def facilities(request):
    return render(request, "vpn/facilities.html", {})

def reach(request):
    return render(request, "vpn/reach.html", {})

def functionaries(request):
    return render(request, "vpn/functionaries.html", {})

def director(request):
    return render(request, "vpn/director.html", {})

def office(request):
    return render(request, "vpn/office.html", {})

def placement(request):
    return render(request, "vpn/placement.html", {})

def record(request):
    return render(request, "vpn/record.html", {})

def recruiters(request):
    return render(request, "vpn/recruiters.html", {})

def internship(request):
    return render(request, "vpn/internship.html", {})

def opportunities(request):
    return render(request, "vpn/opportunities.html", {})

def handler404(request):
    return render(request, 'vpn/404.html', status=404)

def handler500(request):
    return render(request, 'vpn/500.html', status=500)
