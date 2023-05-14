from django.shortcuts import render
from django.http import HttpResponse
from .templates import *

def home(request):
    return render(request, 'home.html')


