from django.shortcuts import render, redirect
from patients.models import Patients
from authentication.models import Registration
from .models import patientRecords

# Create your views here.
def patientsDiagnosisView(request):
    success = ""
    error = ""
    if request.method == "POST":
        addedBy = request.COOKIES['useremail']
        patient = request.POST['patient']
        Triage = request.POST['diagnosis']
        
        pat = Patients.objects.get(id = patient)
        user = Registration.objects.get(Email = addedBy)
        new_diagnosis = patientRecords(
            addedBy = user,
            patient = pat,
            Triage = Triage
        )
        
        new_diagnosis.save()
        
        success = "Patients triage saved successfully"
    
    patients = Patients.objects.all().order_by("-id")
    context = {
        'title': 'Diagnosis Records',
        'patients': patients,
        'success': success,
        'error': error
    }
    
    return render(request,'diagnosis.html', context)