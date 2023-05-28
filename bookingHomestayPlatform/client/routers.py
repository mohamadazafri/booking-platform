from rest_framework.routers import DefaultRouter
from .views import *

homestay_router = DefaultRouter()
homestay_router.register('homestay', HomestayViewSet, basename='homestay')

houseunit_router = DefaultRouter()
houseunit_router.register('house-unit', HouseUnitViewSet, basename='house-unit')

booking_router = DefaultRouter()
booking_router.register('booking-api', BookingViewSet, basename='booking')


