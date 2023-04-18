from django.urls import path
from django.http import HttpResponse
from .views import home,login


urlpatterns=[
    path('',login),
    path('home', home, name='home')
]