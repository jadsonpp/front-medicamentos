from django.db import models


class Alerta(models.Model):
    dataHoraRegistro:str = models.DateField()
    estado:str = models.CharField(max_length=30)
    numeroOnibus:int = models.IntegerField()
    latitude:str = models.CharField(max_length=20)
    longitude:str = models.CharField(max_length=20)
    suspeitoID:int = models.IntegerField()
    urlFoto:str = models.CharField(max_length=400)

