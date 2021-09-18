from django.forms import forms
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Admins, Articulos, Comentarios, Estudiante
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import FormAdministradores, FormArticulos, FormComentarios, FormEstudiante
# Create your views here.

class HomeView(CreateView):
    model=Articulos
    form_class=FormArticulos
    template_name='index.html'
    success_url=reverse_lazy('app1:listar_art')

class CreditosView(CreateView):
    model=Comentarios
    form_class=FormComentarios
    template_name='acercade.html'
    success_url=reverse_lazy('app1:listar_com')

class estudiantesView(CreateView):
    model=Estudiante
    form_class=FormEstudiante
    template_name='estudiantes.html'
    success_url=reverse_lazy('app1:listar_est')

class administradoresView(CreateView):
    model=Admins
    form_class=FormAdministradores
    template_name='administradores.html'
    success_url=reverse_lazy('app1:listar_adm')

class ListarEstudiante(ListView):
    template_name= 'listar_est.html'
    model =  Estudiante

    def get_queryset(self):
        return Estudiante.objects.all()

class ListarAdministradores(ListView):
    template_name= 'listar_adm.html'
    model =  Admins

    def get_queryset(self):
        return Admins.objects.all()

class ListarComentarios(ListView):
    template_name= 'listar_com.html'
    model =  Comentarios

    def get_queryset(self):
        return Comentarios.objects.all()

class ListarArticulos(ListView):
    template_name= 'listar_art.html'
    model =  Articulos

    def get_queryset(self):
        return Articulos.objects.all()


