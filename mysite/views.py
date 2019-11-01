from django.views.generic import TemplateView
from django.shortcuts import render
import requests
import json
from django.shortcuts import get_object_or_404,redirect
from .models import(
    Medicine
)

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
        r[i]['id_medicamento'] = r[i]['_id']
    #rename _id 
    
    #rDict = json.loads(r)
    #rDict
    return render(request, 'freePharma/medicinepage.html', {'medicines': r})


def new_medicine(request):
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


#@login_required
def medicine_update(request,id:str):
    url = "https://api-medicamentos.herokuapp.com/api/medicines/"+str(id)
    r = requests.get(url).json()
    medicine = Medicine(id,r['name'],r['amount'],r['minAmount'],r['lot'],r['validity'],r['description'])
    #medicine.showMedicine()
    form = MedicineForm(instance=medicine)
    if(request.method == 'POST'):
        form = MedicineForm(request.POST,instance=medicine)
        if(form.is_valid()):
            medicine = form.save(commit=False)
            medicine.name = form.cleaned_data["name"]
            medicine.amount = form.cleaned_data["amount"]
            medicine.description = form.cleaned_data["description"]
            medicine.minAmount = form.cleaned_data["minAmount"]
            medicine.lot = form.cleaned_data["lot"]
            medicine.validity = form.cleaned_data["validity"]

            medicine = {
                'name':medicine.name,
                'amount':medicine.amount,
                'description':medicine.description,
                'minAmount':medicine.minAmount,
                'lot':medicine.lot,
                'validity':medicine.validity
            }
            r = requests.put(url,
                    data= json.dumps(medicine),
                    headers = {'content-type':'application/json'})
            
            return redirect ('home')   
    
    return render (request, 'freePharma/update.html', {'form':form})

def medicine_delete(request,id:str):
    #if(request.method == "delete"):

    api:str = 'https://api-medicamentos.herokuapp.com/api/medicines/'+id
    r = requests.delete(api,
                        headers = {'content-type':'application/json'})
    return redirect('home')