import io
import json
import pdb
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import *
from .models import *
import pdfkit
from .templates import *
import os
import requests
import random
import string
import uuid
from datetime import datetime

class HomestayViewSet(ViewSet):
    # queryset = Homestay.objects.all()
    
    def list(self, request):
        queryset = Homestay.objects.all()
        serializers = HomestaySerializer(queryset, many=True)

        return Response(serializers.data)
    
    def create(self, request):
        serializers = HomestaySerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)

    def retrieve(self, request, pk = None):
        queryset = Homestay.objects.get(id = pk)
        serializers = HomestaySerializer(queryset)

        return Response(serializers.data)
    
    def update(self, request, pk = None):
        queryset = Homestay.objects.get(id)
        serializers = HomestaySerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)

    def destroy(self, request, pk = None):
        queryset = Homestay.objects.get(id)
        serializers = HomestaySerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
        return Response(serializers.data)
    
# House unit
class HouseUnitViewSet(ViewSet):
    
    def list(self, request):
        queryset = HouseUnit.objects.all()
        serializers = HouseUnitSerializer(queryset, many=True)

        return Response(serializers.data)
    
    def create(self, request):
        serializers = HouseUnitSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)

    def retrieve(self, request, pk = None):
        queryset = HouseUnit.objects.get(id = pk)
        serializers = HouseUnitSerializer(queryset)

        return Response(serializers.data)
    
    def update(self, request, pk = None):
        queryset = HouseUnit.objects.get(id)
        serializers = HouseUnitSerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)

    def destroy(self, request, pk = None):
        queryset = HouseUnit.objects.get(id)
        serializers = HouseUnitSerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
        return Response(serializers.data)

class BookingViewSet(ViewSet):
    def setMeridian(self, strtime):
        timeSplit = strtime.split(':')

        hours = int(timeSplit[0])
        minutes = int(timeSplit[1])
        if hours > 12 :
            meridian = 'PM'
            hours -= 12
        elif hours < 12 :
            meridian = 'AM'
            if hours == 0 :
                hours = 12
        else :
            meridian = 'PM'

        return strtime + " " + meridian

    def showInvoice(self, request, pk = None, filename = None):
        invoice = Invoice.objects.get(id = pk)

        return HttpResponse(bytes(invoice.content), headers={"Content-Type": "application/pdf",
                                 "Content-Disposition": 'inline; filename=\"' + invoice.title +'.pdf\"',
                                 })

    def list(self, request):
        queryset = Booking.objects.all()
        serializers = BookingSerializer(queryset, many=True)

        return Response(serializers.data)
    
    def create(self, request):
        cust_name = request.POST.get('name')
        houseUnit = request.POST.get('house_unit')
        priceUnit = request.POST.get('price_per_night')
        checkInDate = request.POST.get('check_in_date')
        checkInTime = request.POST.get('check_in_time')
        checkOutDate = request.POST.get('check_out_date')
        checkOutTime = request.POST.get('check_out_time')
        totalAdult = request.POST.get('total_adult')
        totalChild = request.POST.get('total_child')
        purpose = request.POST.get('purpose_of_booking')
        invoiceTitle = str(cust_name) + "--" + str(checkInDate) + "-" + str(checkOutDate) +".pdf"

        total_night = datetime.strptime(checkOutDate, "%Y-%m-%d") - datetime.strptime(checkInDate, "%Y-%m-%d")
        invoice_check_in_date = (datetime.strptime(checkInDate, "%Y-%m-%d")).strftime("%d %b, %Y ")
        invoice_check_out_date = (datetime.strptime(checkOutDate, "%Y-%m-%d")).strftime("%d %b, %Y ")

        price_total_night = total_night.days * float(priceUnit)

        cust = Customer.objects.create(name=cust_name)

        house = HouseUnit.objects.get(id = int(houseUnit))

        invoice_date = datetime.now().strftime("%d %B, %Y (%H:%M)")

        confirmationCode = random.choice(string.ascii_uppercase) + str(random.randint(1000,9999))

        invoiceNumber = random.randint(1000,9999)

        context = {"guest_name" : cust_name, "house_unit": houseUnit, "check_in_date": invoice_check_in_date,"check_in_time": self.setMeridian(checkInTime), "check_out_date": invoice_check_out_date, "check_out_time": self.setMeridian( checkOutTime), "total_adult": totalAdult, "total_kids": totalChild, 'total_night': total_night.days, 'price_per_night': float(priceUnit), 'price_total_night': price_total_night, "invoice_date": invoice_date, "confirmation_code": confirmationCode, "invoice_number": invoiceNumber}

        invoice_HTML = render(request, 'invoiceTemplate.html', context).content.decode('UTF-8')

        # Get the absolute path of the current file (views.py)
        current_file_path = os.path.abspath(__file__)
        
        # Get the directory path containing the current file
        current_directory = os.path.dirname(current_file_path)
        
        # Construct the relative path to wkhtmltopdf.exe
        wkhtmltopdf_path = os.path.join(current_directory, 'wkhtmltopdf\\bin\\wkhtmltopdf.exe')

        pdf_config = pdfkit.configuration(wkhtmltopdf = wkhtmltopdf_path)

        invoicePDF = pdfkit.from_string(invoice_HTML, configuration=pdf_config, options={"--enable-local-file-access" : True})

        new_invoice = Invoice(title = invoiceTitle,
                              content = invoicePDF,
                              receipt_number = invoiceNumber)
        
        new_invoice.save()

        new_book = Booking(customer_id = cust.id,
                            house_unit_id = house.id,
                            invoice_id = new_invoice.id,
                            check_in_date = checkInDate,
                            check_in_time = checkInTime,
                            check_out_date = checkOutDate,
                            check_out_time = checkOutTime,
                            total_adult = totalAdult,
                            total_child = totalChild,
                            purpose_of_booking = purpose,
                            confirmation_code = confirmationCode
                            )
        
        new_book.save()
        invoice_serializer = InvoiceSerializer(new_invoice)
        
        return Response({"success": "done", "invoice_detail": invoice_serializer.data})


    def retrieve(self, request, pk = None):
        queryset = Booking.objects.get(id = pk)
        serializers = BookingSerializer(queryset)

        return Response(serializers.data)
    
    def update(self, request, pk = None):
        queryset = Booking.objects.get(id)
        serializers = BookingSerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)

    def destroy(self, request, pk = None):
        queryset = Booking.objects.get(id)
        serializers = BookingSerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
        return Response(serializers.data)
    
class CustomerViewSet(ViewSet):

    def list(self, request):
        queryset = Customer.objects.all()
        serializers = CustomerSerializer(queryset, many=True)

        return Response(serializers.data)
    
    def create(self, request):
        serializers = CustomerSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)

    def retrieve(self, request, pk = None):
        queryset = Customer.objects.get(id = pk)
        serializers = CustomerSerializer(queryset)

        return Response(serializers.data)
    
    def update(self, request, pk = None):
        queryset = Customer.objects.get(id)
        serializers = CustomerSerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)

    def destroy(self, request, pk = None):
        queryset = Customer.objects.get(id)
        serializers = CustomerSerializer(queryset, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
        return Response(serializers.data)



    



