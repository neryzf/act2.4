"""tarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import HomeView,CreditosView, ListarAdministradores, ListarArticulos, ListarComentarios, ListarEstudiante,administradoresView,estudiantesView

app_name='app1'

urlpatterns = [
    path('index/', HomeView.as_view(), name='home'),
    path('creditos/', CreditosView.as_view(), name='creditos'),
    path('administradores/', administradoresView.as_view(), name='administradores'),
    path('estudiantes/', estudiantesView.as_view(), name='estudiantes'),
    path('listest/', ListarEstudiante.as_view(), name='listar_est'),
    path('listadm/', ListarAdministradores.as_view(), name='listar_adm'),
    path('listcom/', ListarComentarios.as_view(), name='listar_com'),
    path('listart/', ListarArticulos.as_view(), name='listar_art'),
]
