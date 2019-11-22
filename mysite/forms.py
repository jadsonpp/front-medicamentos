from django.forms import ModelForm
from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
    Patient,
    Medicine
)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class MedicineForm(ModelForm):
    name:str = forms.CharField(required=False)
    amount:int= forms.IntegerField(required=False)
    minAmount:int = forms.IntegerField(required=False)
    lot:str = forms.CharField(required=False)
    validity:str = forms.CharField(required=False)
    description:str=forms.CharField(widget=forms.Textarea,required=False)
    class Meta:
        model = Medicine
        fields = '__all__'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
