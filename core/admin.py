from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Turno


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'disponible', 'matricula']
    list_filter = ['especialidad', 'disponible']
    search_fields = ['nombre', 'matricula']


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni', 'telefono']
    search_fields = ['nombre', 'apellido', 'dni']


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'medico', 'fecha_hora', 'estado']
    list_filter = ['estado', 'medico', 'fecha_hora']
    search_fields = ['paciente__nombre', 'paciente__apellido', 'medico__nombre']