import pdb
from django.shortcuts import render
from django.http import HttpResponse
from .templates import *
from client.models import *
from client.serializers import *
import requests
from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime

def home(request):
    queryset = HouseUnit.objects.all()
    context = {
        'house_unit_data' : queryset 
    }
    return render(request, 'home.html', context)

def booking(request):
    book_query = Booking.objects.all().order_by("check_in_date")
    book_serializer = BookingCustomerSerializer(book_query, many=True)  

    for book in book_serializer.data:
        arrival_date = book['check_in_date'] +"T" + book['check_in_time'] + "Z"
        check_out_date = book['check_out_date'] +"T" + book['check_out_time'] + "Z"

        current_date = datetime.now()
        arrival_date = datetime.strptime(arrival_date, "%Y-%m-%dT%H:%M:%SZ")
        check_out_date = datetime.strptime(check_out_date, "%Y-%m-%dT%H:%M:%SZ")

        arrival_days_left = (arrival_date - current_date).days

        book.update({"arrival_days_left": arrival_days_left})
        book.update({"check_in_date": arrival_date.strftime('%d %b, %Y')})
        book.update({"check_out_date": check_out_date.strftime('%d %b, %Y')})

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

