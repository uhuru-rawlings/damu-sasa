from django.shortcuts import render, HttpResponse
from patientsrecords.models import patientRecords
from patients.models import Patients
from rest_framework import serializers
from rest_framework.decorators import api_view
from .serializer import PatientsSerializer,PatientsRecordsSerializer

# Create your views here.
api_view('GET')
def get_all_patients(request):
    all_users = Patients.objects.all()
    
    if all_users:
        all_users = all_users
    else:
        all_users = []    
    serialize = PatientsSerializer(all_users, many=True)
    
    return HttpResponse(serialize)
        

    