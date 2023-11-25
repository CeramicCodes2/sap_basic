from django.shortcuts import render,get_object_or_404,redirect
from .models import Persona
from .Forms import PersonaForm
from django.forms import modelform_factory

# Create your views here.
def detalle_personas(request,id:int):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'personas/detalle.html',{"persona":persona})

#PersonForm = modelform_factory(Persona,exclude=[])
PersonForm = PersonaForm
def newPersona(request):
    context = {
        'newPersonForm':PersonForm(),
        'message':''
    }
    if request.method == 'POST':
        # procesar datos y guardar
        formPersona = PersonForm(request.POST)
        # con esta sintaxis obtenemos informacion de 
        # cada uno de los parametros enviados del cliente hacia
        # nuestro servidor
        # debemos validar los datos y almacenar en la base de datos
        
        if formPersona.is_valid():
            # usamos esta funcion para validar informacion
            # ahora guardamos informacion
            formPersona.save()
            return redirect('index')
        
        context['message'] = 'Error de llenado !'


    return render(request,'personas/nuevo.html',context=context)
def editarPersona(request,id):
    persona_object = get_object_or_404(Persona,pk=id)
    if request.method == "POST":
        # transaccion post envio de datos del ususario
        formPerson = PersonaForm(request.POST,instance=persona_object)
        # debemos especificar con instance que 
        # vamos a actualizar un campo por que si no django no lo hace
        
        if formPerson.is_valid():
            formPerson.save()
            # django reconoce que si ya se tiene un id
            # se realiza un update no un insert
            
            return redirect('index')
    # recperacion de persona
    context = {
        # para consturir el formulario en base a los datos
        # de persona debemos utilizar instance para indicar que se 
        # realizara una instancia
        # debemos agregar un campo de id para que django
        # entienda de que estamos actualizando y no insertando valores
        
        'editForm':PersonaForm(instance=persona_object)
    }
    # debemos usar el =
    
    return render(request,'personas\editar.html',context)