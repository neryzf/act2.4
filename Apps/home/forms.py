from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Admins, Articulos, Comentarios, Estudiante
class FormEstudiante(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=[
            'nombre',
            'apellido',
            'direccion',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'direccion':'Direccion', 
        }

class FormAdministradores(forms.ModelForm):
    class Meta:
        model=Admins
        fields=[
            'nombre',
            'apellido',
            'direccion',
        ]
        labels={
          'nombre':'Nombre',
          'apellido':'Apellido',
          'direccion':'Direccion',  
        }

class FormArticulos(forms.ModelForm):
    class Meta:
        model=Articulos
        fields=[
            'titulo',
            'contenido',
            'nombre',
        ]
        labels={
          'titulo':'Titulo',
          'contenido':'Contenido',
          'nombre':'Nombre',  
        }

class FormComentarios(forms.ModelForm):
    class Meta:
        model=Comentarios
        fields=[
            'contenido',
            'nombre',
        ]
        labels={
            'contenido':'Contenido',
            'nombre':'Nombre',
        }