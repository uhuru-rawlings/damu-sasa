from django.contrib import admin
from django.urls import path
from authentication.views import loginView,signupView,resetView
from patients.views import patientsView,searchPatientView,addPatientsView,updatePatientsView,daletePatientsView
from patientsrecords.views import patientsDiagnosisView
from api.views import get_all_patients,get_all_patients_records


urlpatterns = [
    path('', loginView, name='login'),
    path('signup', signupView, name='signup'),
    path('reset', resetView, name='reset-password'),
    path('dashboard', patientsView, name='dashboard'),
    path('patients/search', searchPatientView, name='search'),
    path('patients/add-patients', addPatientsView, name='add-patients'),
    path('patients/update-patients/<int:id>', updatePatientsView, name='update-patients'),
    path('patients/delete-patients/<int:id>', daletePatientsView, name='delete-patients'),
    
    path('diagnosis/', patientsDiagnosisView, name='diagnosis'),
    path('admin/', admin.site.urls),
    # api link
    path('api/patients', get_all_patients),
    path('api/records', get_all_patients_records),
]
