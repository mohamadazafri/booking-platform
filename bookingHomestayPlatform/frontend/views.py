import pdb
from django.shortcuts import render
from django.http import HttpResponse
from .templates import *
from client.models import *
from client.serializers import *

def home(request):
    queryset = HouseUnit.objects.all()
    context = {
        'house_unit_data' : queryset 
    }
    return render(request, 'home.html', context)

def booking(request):
    queryset = Booking.objects.all()
    context = {
        'booking_data' : queryset,
    }
    return render(request, 'booking.html', context)


