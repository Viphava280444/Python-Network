from django.shortcuts import render
from django.http import HttpResponse
from .messageTest import calTen
from .messageTest import calGate



# Create your views here.

def home(request):
    return HttpResponse(f"INDEX")

def login(request):
    return HttpResponse("LOGIN")