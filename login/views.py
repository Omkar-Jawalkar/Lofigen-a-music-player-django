from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def adminlogin(response):    
    if response.method == "POST":
        email = response.POST.get('admin', None)
        password = response.POST.get('pass', None)
        if email and password:
            user = authenticate(username=email, password=password)
            login(response, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            print("User Dosent exist")

    return render(response,"login/adminlogin.html",{})

def userlogin(response):
    return render(response,"login/userlogin.html", {})
