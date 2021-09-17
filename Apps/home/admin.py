from django.contrib import admin
from .models import Admins, Articulos, Cliente, Comentarios, Estudiante, TipoCliente,Venta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Venta)
admin.site.register(Estudiante)
admin.site.register(Admins)
admin.site.register(Comentarios)
admin.site.register(Articulos)