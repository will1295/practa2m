from django.shortcuts import render
from .formularios.regisform import RegUser
from django.http import HttpResponseRedirect

def Home(request):
    return render(request,"home.html")

def Registrar(request):
    if(request.method=="POST"):
        formulario=RegUser(request.POST)
        if(formulario.is_valid()):
            formulario.guardar()
            return HttpResponseRedirect("/")
    else:
        formulario=RegUser()
        return render(request,"registro.html",{"form":formulario})
