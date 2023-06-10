import pdb
from django.shortcuts import render
from django.http import HttpResponse
from .templates import *
from client.models import *
from client.serializers import *
import requests
from PyPDF2 import PdfFileReader, PdfFileWriter

def home(request):
    queryset = HouseUnit.objects.all()
    context = {
        'house_unit_data' : queryset 
    }
    return render(request, 'home.html', context)

def booking(request):
    book_query = Booking.objects.all()
    book_serializer = BookingCustomerSerializer(book_query, many=True)    

    print(book_serializer.data)
    context = {
        'booking_data' : book_serializer.data,
    }
    return render(request, 'booking.html', context)

def test(request):
    
    return render(request, 'test.html')

def displayPDF(request):
    responseData = requests.get("https://nsi-live.oss-ap-southeast-3.aliyuncs.com/dmsusersubs/1922/CP22_Pin.1_2021.pdf")
        
    return HttpResponse(responseData.content, 
                        headers={"Content-Type": "application/pdf",
                                 "Content-Disposition": 'inline; filename=\"test.pdf\"',
                                 })

