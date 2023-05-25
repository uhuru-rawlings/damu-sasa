from patients.models import Patients
from patientsrecords.models import patientRecords
from rest_framework import serializers

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'
        
class PatientsRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = patientRecords
        fields = '__all__'