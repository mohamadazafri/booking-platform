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

    def showInvoice(self, request, pk = None, filename = None):
        # cust_query = Customer.objects.get(booking__id = pk)
        # book_query = Booking.objects.get(id = pk)

        invoice = Invoice.objects.get(booking__id = pk)

        return HttpResponse(bytes(invoice.content), headers={"Content-Type": "application/pdf",
                                 "Content-Disposition": 'inline; filename=\"' + invoice.title +'.pdf\"',
                                 })

        # cust_name = "Azafri"
        # house_unit = "1"
        # checkInDate = "27/1/2023"
        # checkOutDate = "30/1/2023"
        # totalAdult = 1
        # totalChild = 0
        # invoiceTitle = "Hello world"
        
        # context = {"cust_name" : cust_name, "house_unit": house_unit, "check_in_date": checkInDate, "check_out_date": checkOutDate, "total_adult": totalAdult, "total_child": totalChild, "invoice_title": invoiceTitle }

        # return render(request, 'invoiceTemplate.html', context)

    def list(self, request):
        queryset = Booking.objects.all()
        serializers = BookingSerializer(queryset, many=True)

        return Response(serializers.data)
    
    def create(self, request):
        pdb.set_trace()
        cust_name = request.POST.get('name')
        houseUNit = request.POST.get('house_unit')
        checkInDate = request.POST.get('check_in_date')
        checkOutDate = request.POST.get('check_out_date')
        totalAdult = request.POST.get('total_adult')
        totalChild = request.POST.get('total_child')
        purpose = request.POST.get('purpose_of_booking')
        invoiceTitle = str(cust_name) + "--" + str(checkInDate) + "-" + str(checkOutDate) +".pdf"

        cust = Customer.objects.create(name=cust_name)

        house = HouseUnit.objects.get(id = int(houseUNit))

        context = {"cust_name" : cust_name, "house_unit": houseUNit, "check_in_date": checkInDate, "check_out_date": checkOutDate, "total_adult": totalAdult, "total_child": totalChild  }

        invoice_HTML = render(request, 'invoiceTemplate.html', context).content.decode('UTF-8')

        # Get the absolute path of the current file (views.py)
        current_file_path = os.path.abspath(__file__)
        
        # Get the directory path containing the current file
        current_directory = os.path.dirname(current_file_path)
        
        # Construct the relative path to wkhtmltopdf.exe
        wkhtmltopdf_path = os.path.join(current_directory, 'wkhtmltopdf\\bin\\wkhtmltopdf.exe')

        pdf_config = pdfkit.configuration(wkhtmltopdf = wkhtmltopdf_path)

        invoicePDF = pdfkit.from_string(invoice_HTML, configuration=pdf_config, options={"--enable-local-file-access" : True})

        receiptNumber = random.randint(1000,9999)
        new_invoice = Invoice(title = invoiceTitle,
                              content = invoicePDF,
                              receipt_number = receiptNumber)
        
        new_invoice.save()

        confirmationCode = random.choice(string.ascii_uppercase) + str(random.randint(1000,9999))

        new_book = Booking(customer_id = cust.id,
                            house_unit_id = house.id,
                            invoice_id = new_invoice.id,
                            check_in_date = checkInDate,
                            check_out_date = checkOutDate,
                            total_adult = totalAdult,
                            total_child = totalChild,
                            purpose_of_booking = purpose,
                            confirmation_code = confirmationCode
                            )
        
        new_book.save()
        
        return Response({"success": "done"})


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
    
    # def test(self, request) :
        
    #     # response = requests.get("https://nsi-live.oss-ap-southeast-3.aliyuncs.com/dmsusersubs/2601/test.pdf")
    #     responseData = requests.get("https://nsi-live.oss-ap-southeast-3.aliyuncs.com/dmsusersubs/1918/test.pdf")

        
    #     # # bytePDF = bytearray(response.content)
    #     data = io.BytesIO()
    #     data.write(responseData.content)
    #     data.seek(0)

    #     response = FileResponse(data.getvalue(), filename="example.pdf")

    #     return response
    
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



    



