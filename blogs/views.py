from django.shortcuts import render
from django.http import HttpResponse
from .messageTest import calTen
from .messageTest import calGate



# Create your views here.

def index(request):
    return HttpResponse(f"""<h1> Hello I Ohm eiei </h1>
    <h1> Hello I Tan eiei </h1>
    <h1> Hello I Bigboss {calGate()} {calTen()}</h1>""")