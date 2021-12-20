from django.contrib import admin
from django.urls import path, include

URLPattern = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),


]