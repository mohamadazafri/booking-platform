from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('test/', views.test, name='test'),
    # path('display-pdf/test.pdf', views.displayPDF, name='displayPDF')
]