import json
import pdb
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import *
from .models import *

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

    def list(self, request):
        queryset = Booking.objects.all()
        serializers = BookingSerializer(queryset, many=True)

        return Response(serializers.data)
    
    def create(self, request):
        cust_serializer = CustomerSerializer(data=request.data)
        cust_serializer.is_valid(raise_exception=True)
        instance = cust_serializer.save()

        data = request.data.copy()
        data.update({'customer': instance.id})        
        booking_serializer = BookingSerializer(data=data)
        booking_serializer.is_valid(raise_exception=True)
        booking_serializer.save()

        return Response('succeed')

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



    



