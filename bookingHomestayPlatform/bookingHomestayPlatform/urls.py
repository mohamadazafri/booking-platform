from django.contrib import admin
from django.urls import path, include
from django.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("frontend.urls")),
    path('api/', include("client.urls")),
]
