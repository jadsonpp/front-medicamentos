from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests
import json
from django.shortcuts import get_object_or_404,redirect


from ..forms import (
    RegisterForm
)

#### everything about user. 
##### login,loggout and register

def login(response):
    return redirect ('/login')

def logout(response):
    return redirect ('/logout')

def registerUser(response):
    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            #return redirect()
    else:
        form = RegisterForm()
    return render(response,"registration/reg.html",{"form":form})


