from django.shortcuts import render
from .models import Company,Employee
from api.models import Company,Employee
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import CompanySerializer,EmployeeSerializer
# Create your views here.
import os
def get_image_url(company):
    if company.upload:
        image_path = os.path.join(settings.MEDIA_ROOT, str(company.upload))
        if os.path.exists(image_path):
            return company.upload.url
    return '/static/default_image.jpg'  # Adjust this line as needed

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    
class EmployeeViewSet(viewsets.ModelViewSet):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     
     
import requests
def home(request):
    response = requests.get("http://127.0.0.1:8000/api/v1/companies/").json()
    return render(request,"index.html",{'response':response})
    