from django.db import models


class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()# tipo de dato int
    pais = models.CharField(max_length=30)
    # para relacionar usamos llave foranea
    def __str__(self):
        return f'{self.calle} {self.no_calle} {self.pais}'
    
    
# Create your models here.
class Persona(models.Model):
    # tipos de datos en https://docs.djangoproject.com/en/4.2/topics/db/models/
    nombre = models.CharField(max_length=30)# maximo de caracteres
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'''{self.id} {self.nombre} {self.email}'''

# cone sto creara una tabla llamada persona
# con nombre apellido y email
# pero debemos de usar python manage.py makemigrations
