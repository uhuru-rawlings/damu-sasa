from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from patientsrecords.models import patientRecords
from patients.models import Patients
from rest_framework import serializers
from rest_framework.decorators import api_view
from .serializer import PatientsSerializer,PatientsRecordsSerializer

# Create your views here.
@api_view(['GET'])
def get_all_patients(request):
    all_users = Patients.objects.all()
    
    if all_users:
        all_users = all_users
    else:
        all_users = []    
    serialize = PatientsSerializer(all_users, many=True)
    
    return Response(serialize.data)

@api_view(['GET'])
def get_all_patients_records(request):
    all_records = patientRecords.objects.all()
    
    if all_records:
        all_records = all_records
    else:
        all_records = []    
    serialize = PatientsRecordsSerializer(all_records, many=True)
    
    return Response(serialize.data)
        

    