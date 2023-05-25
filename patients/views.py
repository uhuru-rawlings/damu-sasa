from django.shortcuts import redirect, render
from .models import Patients
from django.db.models import Q
import random

# Create your views here.
def patientsView(request):
    search = ""
    all_patients = Patients.objects.all().order_by("-id")
    context = {
        'title': 'Patients Dashboard',
        'patients': all_patients
    }
    
    return render(request, 'patients.html', context)

def searchPatientView(request):
    if request.method == "POST":
        search = request.POST.get('user_search')
        
        all_patients = Patients.objects.filter(Q(Fname = search)| Q(Lname = search) | Q(IdNumber = search)).order_by("-id")
        
        context = {
            'title': 'Patients Search Dashboard',
            'patients': all_patients
        }
        
        return render(request, 'search.html', context)
    
def addPatientsView(request):
    error = ""
    success = ""
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        Idnumber = request.POST['Idnumber']
        county = request.POST['county']
        village = request.POST['village']
        
        patient = Patients.objects.filter(IdNumber = Idnumber)
        
        if patient.exists():
            error = "Oops! patient with these records already exist.";
        else:
            range_start = 10**(11-1)
            range_end = (10**11)-1
            
            new_patient = Patients(
                Fname = fname,
                Lname = lname,
                IdNumber = Idnumber,
                PatientsNo = random.randint(range_start,range_end),
                FromTown = county,
                FromVillage = village
            )
            new_patient.save()
            
            success = "patient added successfully."
            
    context = {
        'title': 'Add Records',
        'error': error,
        'success': success
    }
    
    return render(request, 'add-patients.html', context)

def updatePatientsView(request, id):
    success = ""
    error = ""
    patient = Patients.objects.get(id = id)
    
    if request.method == "POST":
        update = request.POST['update']
        fname = request.POST['fname']
        lname = request.POST['lname']
        Idnumber = request.POST['Idnumber']
        county = request.POST['county']
        village = request.POST['village']
        
        patient = Patients.objects.filter(id = update)
        
        if patient.exists():
            new_patient = Patients.objects.get(id = update)
            new_patient.Fname = fname
            new_patient.Lname = lname
            new_patient.IdNumber = Idnumber
            new_patient.FromTown = county
            new_patient.FromVillage = village
            
            new_patient.save()
            
            return redirect('dashboard')
        else:
            error = "Oops! patient with these records already exist."
            
            success = "patient added successfully."
      
    context = {
        'title': 'Update Records',
        'success': success,
        'patient':patient,
        'error': error,
        'id': id
    }
    
    return render(request, 'update-patient.html', context)

def daletePatientsView(request, id):
    
    patient = Patients.objects.get(id = id)
    patient.delete()
    
    return redirect('dashboard')