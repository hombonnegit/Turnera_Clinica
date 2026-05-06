"""
URL routes for pacientes app.
"""
from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.sacar_turno, name='sacar_turno'),
    path('buscar-medicos/', views.buscar_medicos, name='buscar_medicos'),
    path('registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/<int:pk>/', views.detalle_paciente, name='detalle_paciente'),
    path('pacientes/<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('turnos/crear/', views.crear_turno, name='crear_turno'),
    path('turnos/', views.listar_turnos, name='listar_turnos'),
]
