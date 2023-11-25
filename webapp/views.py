from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from personas.models import Persona

def bienvenido(request):
    data = {
        'no_personas':Persona.objects.count(),
        'all_personas':Persona.objects.all()
    }
    return render(request,'bienvenido.html',data)