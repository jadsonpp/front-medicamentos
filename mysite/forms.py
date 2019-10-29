from django.forms import ModelForm
from .models import (
    Patient,
    Medicine
)


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
