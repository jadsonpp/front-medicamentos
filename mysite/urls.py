from django.contrib import admin
from django.urls import path
from .views import (
    home,
    new_medicine,
    medicine_update,
    medicine_delete
)

urlpatterns = [
    path('', home,name='home'),
    path('medicine/new',new_medicine, name="new_medicine"),
    path('medicine/edit/<str:id>/',medicine_update,name="medicine_update"),
    path('medicine/delete/<str:id>/',medicine_delete,name="medicine_delete")
]

'''
    path('aberto',estadoAberto),
    path('fechado',estadoFechado),
    path('cancelado',estadoCancelado),
    path('andamento',estadoAndamento),
    path('alertas', home)
'''