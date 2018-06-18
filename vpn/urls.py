"""training and placement portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^facilities/', views.facilities, name='facilities'),
    url(r'^how-to-reach/', views.reach, name='reach'),
    url(r'^functionaries/', views.functionaries, name='functionaries'),
    url(r'^directors-desk/', views.director, name='director'),
    url(r'^training-Placement-Office/', views.office, name='office'),
    url(r'^placement-procedure/', views.placement, name='placement'),
    url(r'^placement-record/', views.record, name='record'),
    url(r'^proud-recruiters/', views.recruiters, name='recruiters'),
    url(r'^internship-procedure/', views.internship, name='internship'),
    url(r'^training-internship-opportunities/', views.opportunities, name='opportunities'),
]
