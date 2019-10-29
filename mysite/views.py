from django.views.generic import TemplateView
from django.shortcuts import render
import requests
import json
from .forms import (
    PatientForm,
    MedicineForm
)


def home(request):
    url = "https://api-medicamentos.herokuapp.com/api/medicines"
    r = requests.get(url).json()
    for i in range(len(r)):
        dataHora = r[i]['validity'].split("T")
        data = dataHora[0]
        r[i]['validade'] = data
    
    return render(request, 'freePharma/medicinepage.html', {'medicines': r})


def teste(request):
    form = MedicineForm(request.POST)
    
    #getting data from a form
    if form.is_valid():
        name = form.cleaned_data["name"]
        amount = form.cleaned_data["amount"]
        description = form.cleaned_data["description"]
        minAmount = form.cleaned_data["minAmount"]
        lot = form.cleaned_data["lot"]
        validity = form.cleaned_data["validity"]
        #Coleta os dados do formulário
        medicine = {
            'name':name,
            'amount':amount,
            'description':description,
            'minAmount':minAmount,
            'lot':lot,
            'validity':validity
        }
        #sending
        if(request.method=="POST"):
            #rota de post
            api:str = 'https://api-medicamentos.herokuapp.com/api/medicines'
            r = requests.post(api,
                    data= json.dumps(medicine),
                    headers = {'content-type':'application/json'})
            return render (request, 'freePharma/test.html', {'form':form,'medicine':medicine})
    else:
        return render (request, 'freePharma/test.html', {'form':form})

def testeLocal(request):
    form = MedicineForm(request.POST)
    
    #getting data from a form
    if form.is_valid():
        name = form.cleaned_data["name"]
        amount = form.cleaned_data["amount"]
        description = form.cleaned_data["description"]
        minAmount = form.cleaned_data["minAmount"]
        lot = form.cleaned_data["lot"]
        validity = form.cleaned_data["validity"]
        #Coleta os dados do formulário
        medicine = {
            'name':name,
            'amount':amount,
            'description':description,
            'minAmount':minAmount,
            'lot':lot,
            'validity':validity
        }
        #sending
        if(request.method=="POST"):
            #rota de post
            
            api:str = 'http://localhost:3000/api/medicines'
            r = requests.post(api,
                data=json.dumps(medicine),
                headers = {'content-type':'application/json'}
            )
            return render (request, 'freePharma/test.html', {'form':form,'medicine':medicine})
    else:
        return render (request, 'freePharma/test.html', {'form':form})