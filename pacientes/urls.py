"""
URL routes for pacientes app.
"""
from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.sacar_turno, name='sacar_turno'),
    path('buscar-medicos/', views.buscar_medicos, name='buscar_medicos'),
]
