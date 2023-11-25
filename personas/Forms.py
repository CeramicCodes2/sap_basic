from django.forms import ModelForm,EmailInput
from personas.models import Persona
class PersonaForm(ModelForm):
    class Meta:
        ''' 
        aqui indicamos campos importantes y
        el modelo que se usara
        '''
        model = Persona
        fields = '__all__'
        # indicaremos que utilizaremos todos los atributos
        # del modelo persona
        # indicaremos el tipo de campo que se usara para
        # el formulario
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }# tipo de dato y valdiaciones en html
        # colocamos atributos