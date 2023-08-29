from django.shortcuts import render,redirect

from user.models import UserClass
from .form import Inscription,InscriptionUser

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    # ------------LoginForm3---------------

    if request.method == 'POST':
        dataForm = Inscription(request.POST)
        if dataForm.is_valid():
            dataForm.save()
    return render(request,'index.html',{'lf':Inscription})

def acceuil(request):
    return render(request,'accueil.html')

def register(request):
    registered = False
    if request.method == 'POST':
        prd_form = Inscription(data=request.POST)
        form = InscriptionUser(data=request.POST)
        if form.is_valid() and prd_form.is_valid() :
            prd_user = prd_form.save()
            prd_user.save()
            user = form.save(commit=False)
            user.user = prd_user
            user.save()
            registered = True
            messages.success(request,'Votre compte a été bien créer')
            return HttpResponseRedirect('login')
        else:
            messages.error(request,"erreur")
            print(prd_form.errors,form.errors)
    else:    
        prd_form = Inscription()
        form = InscriptionUser()    
    content = {
        'registered':registered,
        'form1':prd_form,
        'form2':form
    }
    return render(request,'register.html', content)


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,'bienvenu')
            return redirect('acceuil')  
        else:
            messages.error(request,"erreur d'authentification")
              


    return render(request,'login.html')


@login_required
def deconnection(request):
    logout(request)