from django.db import models
from authentication.models import Registration
from patients.models import Patients
# Create your models here.
class patientRecords(models.Model):
    addedBy = models.ForeignKey(Registration, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    Triage = models.CharField(max_length=2000)
    dateAdded = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'patientRecords'
    
    def __str__(self):
        return self.Triage