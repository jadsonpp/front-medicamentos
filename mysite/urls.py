from django.contrib import admin
from django.urls import path
from .views import medicine
from .views import login

urlpatterns = [
    path('',login.login, name="loginUser"),
    path('logout',login.logout, name="logout"),
    path('register',login.registerUser,name="register"),
    path('h', medicine.home,name='home'),
    path('medicine/new',medicine.new_medicine, name="new_medicine"),
    path('medicine/edit/<str:id>/',medicine.medicine_update,name="medicine_update"),
    path('medicine/delete/<str:id>/',medicine.medicine_delete,name="medicine_delete")
]
