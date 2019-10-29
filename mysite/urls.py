from django.contrib import admin
from django.urls import path
from .views import (
    home,
    teste

) #,estadoAberto,estadoCancelado,estadoFechado,estadoAndamento
 
urlpatterns = [
    path('', home),
    path('teste',teste, name="teste")
]

'''
    path('aberto',estadoAberto),
    path('fechado',estadoFechado),
    path('cancelado',estadoCancelado),
    path('andamento',estadoAndamento),
    path('alertas', home)
'''