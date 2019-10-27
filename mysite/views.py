from django.shortcuts import render
import requests
import json


def home(request):
    url = "https://api-medicamentos.herokuapp.com/api/medicines"
    r = requests.get(url).json()
    for i in range(len(r)):
        dataHora = r[i]['validity'].split("T")
        data = dataHora[0]
        r[i]['validade'] = data
    
    return render(request, 'freePharma/medicinepage.html', {'medicines': r})
'''
def estadoAberto(request):
    url = "https://alerta-api.azurewebsites.net/api/alertas/aberto"
    r = requests.get(url).json()
    for i in range(len(r)):
        dataHora = r[i]['dataHoraRegistro'].split("T")
        data = dataHora[0]
        hora = dataHora[1]
        r[i]['time'] = data + " " + hora
        r[i]['localizacao'] = str(r[i]['latitude']) + ' , '+ str(r[i]['longitude'])
    return render(request, 'lookatme/alertpage.html', {'alertas': r})

def estadoFechado(request):
    url = "https://alerta-api.azurewebsites.net/api/alertas/fechado"
    r = requests.get(url).json()
    for i in range(len(r)):
        dataHora = r[i]['dataHoraRegistro'].split("T")
        data = dataHora[0]
        hora = dataHora[1]
        r[i]['time'] = data + " " + hora
        r[i]['localizacao'] = str(r[i]['latitude']) + ' , '+ str(r[i]['longitude'])
    return render(request, 'lookatme/fechado_cancelado.html', {'alertas': r})

def estadoAndamento(request):
    url = "https://alerta-api.azurewebsites.net/api/alertas/andamento"
    r = requests.get(url).json()
    for i in range(len(r)):
        dataHora = r[i]['dataHoraRegistro'].split("T")
        data = dataHora[0]
        hora = dataHora[1]
        r[i]['time'] = data + " " + hora
        r[i]['localizacao'] = str(r[i]['latitude']) + ' , '+ str(r[i]['longitude'])
    return render(request, 'lookatme/alertpage.html', {'alertas': r})

def estadoCancelado(request):
    url = "https://alerta-api.azurewebsites.net/api/alertas/cancelado"
    r = requests.get(url).json()
    for i in range(len(r)):
        dataHora = r[i]['dataHoraRegistro'].split("T")
        data = dataHora[0]
        hora = dataHora[1]
        r[i]['time'] = data + " " + hora
        r[i]['localizacao'] = str(r[i]['latitude']) + ' , '+ str(r[i]['longitude'])
    return render(request, 'lookatme/fechado_cancelado.html', {'alertas': r})

'''