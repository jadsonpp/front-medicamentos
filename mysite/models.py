from django.db import models
from django.urls import reverse

class Medicine(models.Model):
    name:str = models.CharField(max_length=255)
    amount:int= models.IntegerField()
    minAmount:int = models.IntegerField()
    lot:str = models.CharField(max_length=255)
    validity:str = models.CharField(max_length=30)
    description:str=models.CharField(max_length=400)

    def showMedicine(self):
        print(self.name)
        print(self.amount)
        print(self.minAmount)
        print(self.lot)
        print(self.validity)
        print(self.description)
    

    '''def get_url(self):
        return reverse('')
    '''
class Patient(models.Model):
    
    name:str = models.CharField(max_length=30)
    susCard:str = models.CharField(max_length=30)
    address:str = models.CharField(max_length=30)

