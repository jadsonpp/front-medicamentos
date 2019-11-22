from django.contrib import admin
from django.urls import path
from .views import (
    home,
    new_medicine,
    medicine_update,
    medicine_delete,
    registerUser
)

urlpatterns = [
    path('',registerUser,name="login"),
    path('h', home,name='home'),
    path('medicine/new',new_medicine, name="new_medicine"),
    path('medicine/edit/<str:id>/',medicine_update,name="medicine_update"),
    path('medicine/delete/<str:id>/',medicine_delete,name="medicine_delete")
]
