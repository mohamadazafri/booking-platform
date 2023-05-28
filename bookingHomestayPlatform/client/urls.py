from django.urls import path, include
from . import views
from .routers import *
from .views import *

urlpatterns = [
    path('', include(homestay_router.urls)),
    path('', include(booking_router.urls)),
    path('', include(houseunit_router.urls)),
    # path('booking/', BookingViewSet.as_view({'post': 'create'}), name='booking-create')
]


