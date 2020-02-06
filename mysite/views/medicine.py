from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests
import json
from django.shortcuts import get_object_or_404,redirect
from ..models import(
    Medicine
)

from ..forms import (
    MedicineForm
)


@login_required
# List of medicines
def home(request):
    #Take the information on api and transform on json
    url = "https://api-medicamentos.herokuapp.com/api/medicines"
    r = requests.get(url).json()
    #Adjust the time (remove unnecessary part of time)
    for i in range(len(r)):
        dataHora = r[i]['validity'].split("T")
        data = dataHora[0]
        r[i]['validade'] = data
        r[i]['id_medicamento'] = r[i]['_id']
    #render the new information into medicine page.
    return render(request, 'freePharma/medicinepage.html', {'medicines': r})
    
#Adding a new Medicine into a database.
@login_required
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
        #parse formulare data into medicine
        medicine = {
            'name':name,
            'amount':amount,
            'description':description,
            'minAmount':minAmount,
            'lot':lot,
            'validity':validity
        }
        #sending datas to database.
        if(request.method=="POST"):
            api:str = 'https://api-medicamentos.herokuapp.com/api/medicines'
            r = requests.post(api,
                    data= json.dumps(medicine),
                    headers = {'content-type':'application/json'})
            return redirect ('home')
    #
    return render (request, 'freePharma/createMedicine.html', {'form':form})

#Update some information from a medicie.
@login_required
def medicine_update(request,id:str):
    #Get Medicine informations and converte to a medicine class.
    url = "https://api-medicamentos.herokuapp.com/api/medicines/"+str(id)
    r = requests.get(url).json()
    medicine = Medicine(id,r['name'],r['amount'],r['minAmount'],r['lot'],r['validity'],r['description'])
    #show this information in a form
    form = MedicineForm(instance=medicine)
    #Get the new update information.
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
            #Converte this information into a medicine class
            medicine = {
                'name':medicine.name,
                'amount':medicine.amount,
                'description':medicine.description,
                'minAmount':medicine.minAmount,
                'lot':medicine.lot,
                'validity':medicine.validity
            }
            #sending this new information to a update route.
            r = requests.put(url,
                    data= json.dumps(medicine),
                    headers = {'content-type':'application/json'})
            return redirect ('home')   
        #
    #
    
    return render (request, 'freePharma/updateMedicine.html', {'form':form})

#Delete the medicine.
@login_required
def medicine_delete(request,id:str):
    api:str = 'https://api-medicamentos.herokuapp.com/api/medicines/'+id
    r = requests.delete(api,
                        headers = {'content-type':'application/json'})
    return redirect('home')