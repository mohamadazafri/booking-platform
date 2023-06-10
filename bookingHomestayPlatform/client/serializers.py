import os
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import serializers
from .models import *
import pdfkit

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class HomestaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Homestay
        fields = '__all__'
        
class HouseUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseUnit
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BookingCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 2
        
class BookingSaveSerializer(serializers.Serializer):
    invoice_content = serializers.CharField()

    def save(self, request):
        cust_serializer = CustomerSerializer(data=request.data)
        cust_serializer.is_valid(raise_exception=True)
        instance = cust_serializer.save()

        context = {"hello": "world"}
        invoice_HTML = render(request, 'invoiceTemplate.html', context).content.decode('UTF-8')

        # Get the absolute path of the current file (views.py)
        current_file_path = os.path.abspath(__file__)
        
        # Get the directory path containing the current file
        current_directory = os.path.dirname(current_file_path)
        
        # Construct the relative path to wkhtmltopdf.exe
        wkhtmltopdf_path = os.path.join(current_directory, 'wkhtmltopdf\\bin\\wkhtmltopdf.exe')

        pdf_config = pdfkit.configuration(wkhtmltopdf = wkhtmltopdf_path)

        invoice_PDF = pdfkit.from_string(invoice_HTML, configuration=pdf_config)

        data = request.data.copy()
        data.update({'customer': instance.id, 'invoice_content': invoice_PDF})  