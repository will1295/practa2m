from django.contrib import admin
from django.urls import path
from app1.views import Home,Registrar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home),
    path('registro/',Registrar)
]
