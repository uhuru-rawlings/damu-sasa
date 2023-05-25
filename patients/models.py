from django.db import models

# Create your models here.
class Patients(models.Model):
    Fname       = models.CharField(max_length=255)
    Lname       = models.CharField(max_length=255)
    IdNumber    = models.CharField(max_length=255, null=True)
    PatientsNo  = models.CharField(max_length=255)
    FromTown    = models.CharField(max_length=255)
    FromVillage = models.CharField(max_length=255)
    lastVisit = models.DateTimeField(auto_now=True)
    dateAdded = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Patients'
    
    def __str__(self):
        return self.Fname