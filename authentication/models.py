from django.db import models

# Create your models here.
class Registration(models.Model):
    Fullname  = models.CharField(max_length=255,null=False)
    Email     = models.EmailField(max_length=255,null=False)
    Password  = models.CharField(max_length=500,null=False)
    LastLogin = models.DateTimeField(null=True)
    DateAdded = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Registration'
    
    def __str__(self):
        return self.Fullname