from django.db import models

class Medicine(models.Model):
    #idMedicines:str = models.CharField(max_length=255)
    name:str = models.CharField(max_length=255)
    amount:int= models.IntegerField()
    minAmount:int = models.IntegerField()
    lot:str = models.CharField(max_length=255)
    validity:str = models.CharField(max_length=30)
    #validity:str = models.DateField()
    description:str=models.TextField()
    
class Patient(models.Model):
    idPatient:str = models.CharField(max_length=50)
    name:str = models.CharField(max_length=30)
    susCard:str = models.CharField(max_length=30)
    address:str = models.CharField(max_length=30)

