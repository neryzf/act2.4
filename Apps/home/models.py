from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    direccion=models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Cliente(models.Model):
    doc = (
    ('D','DPI'),
    ('C','CEDULA'),

    )
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=200)
    nacimiento =models.DateField()
    tipo = models.ForeignKey(
        'TipoCliente',
        on_delete= models.CASCADE,
        default=1,
        )
    documento = models.CharField(
        max_length=20,
        choices=doc,
        default="D")
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class TipoCliente(models.Model):
    tipo =models.CharField(max_length=10)
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s ' % (self.tipo)

class Venta(models.Model):
    cliente = models.ManyToManyField(Cliente)
    fecha = models.DateField()
    def __str__(self):
        return '%s ' % (self.fecha)

class Admins(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    direccion=models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Comentarios(models.Model):
    contenido=models.TextField(max_length=200)
    creacion =models.DateField(auto_now_add=True)
    nombre =  models.ForeignKey(
        'Estudiante',
        on_delete= models.CASCADE,
        default=1,
    )
    def __str__(self):
        return '%s' % (self.contenido)

class Articulos(models.Model):
    titulo=models.CharField(max_length=30)
    creacion =models.DateField(auto_now_add=True)
    contenido =  models.ForeignKey(
        'Comentarios',
        on_delete= models.CASCADE,
        default=1,
    )
    nombre =  models.ForeignKey(
        'Estudiante',
        on_delete= models.CASCADE,
        default=1,
    )
    admin =  models.ForeignKey(
        'Admins',
        on_delete= models.CASCADE,
        default=1,
    )
    def __str__(self):
        return '%s' % (self.titulo)

