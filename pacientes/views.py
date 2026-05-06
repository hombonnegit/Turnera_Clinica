from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db.models import Q
from core.models import Medico, Especialidad, Paciente, Turno
from .forms import PacienteForm, TurnoForm
import json


def sacar_turno(request):
    """Renderiza el formulario de reserva de turnos"""
    pacientes = Paciente.objects.all()
    especialidades = Especialidad.objects.all()
    return render(request, 'pacientes/sacar_turno.html', {
        'pacientes': pacientes,
        'especialidades': especialidades
    })


def buscar_medicos(request):
    """Busca médicos por especialidad vía AJAX/HTMX"""
    especialidad_nombre = request.GET.get('especialidad')

    if not especialidad_nombre:
        response_data = {'error': 'Especialidad no proporcionada'}
        return HttpResponse(json.dumps(response_data, ensure_ascii=False), status=400, content_type='application/json; charset=utf-8')

    try:
        especialidad = Especialidad.objects.get(nombre=especialidad_nombre)
        medicos = Medico.objects.filter(especialidad=especialidad, disponible=True)
    except Especialidad.DoesNotExist:
        response_data = {'error': 'Especialidad no encontrada'}
        return HttpResponse(json.dumps(response_data, ensure_ascii=False), status=404, content_type='application/json; charset=utf-8')

    html = '<select name="medico" class="w-full p-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-indigo-500">'
    for medico in medicos:
        html += f'<option value="{medico.id}">{medico.nombre}</option>'
    html += '</select>'

    response_data = {'html': html}
    return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type='application/json; charset=utf-8')


def registrar_paciente(request):
    """Formulario para registrar un nuevo paciente"""
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()
            messages.success(request, f'¡{paciente.nombre} registrado exitosamente!')
            return redirect('pacientes:listar_pacientes')
    else:
        form = PacienteForm()
    
    return render(request, 'pacientes/registrar_paciente.html', {'form': form})


def listar_pacientes(request):
    """Listado de todos los pacientes"""
    search = request.GET.get('q', '')
    
    if search:
        pacientes = Paciente.objects.filter(
            Q(nombre__icontains=search) | 
            Q(apellido__icontains=search) |
            Q(dni__icontains=search)
        ).order_by('apellido', 'nombre')
    else:
        pacientes = Paciente.objects.all().order_by('apellido', 'nombre')
    
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes, 'search': search})


def detalle_paciente(request, pk):
    """Detalle de un paciente con sus turnos"""
    paciente = get_object_or_404(Paciente, pk=pk)
    turnos = Turno.objects.filter(paciente=paciente).order_by('-fecha_hora')
    
    return render(request, 'pacientes/detalle_paciente.html', {
        'paciente': paciente,
        'turnos': turnos
    })


def editar_paciente(request, pk):
    """Editar datos del paciente"""
    paciente = get_object_or_404(Paciente, pk=pk)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente actualizado exitosamente')
            return redirect('pacientes:detalle_paciente', pk=paciente.pk)
    else:
        form = PacienteForm(instance=paciente)
    
    return render(request, 'pacientes/editar_paciente.html', {
        'form': form,
        'paciente': paciente
    })


def crear_turno(request):
    """Crear un nuevo turno"""
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.estado = 'confirmado'
            turno.save()
            messages.success(request, '¡Turno reservado exitosamente!')
            return redirect('pacientes:listar_turnos')
    else:
        form = TurnoForm()
    
    return render(request, 'pacientes/crear_turno.html', {'form': form})


def listar_turnos(request):
    """Listado de todos los turnos"""
    turnos = Turno.objects.all().order_by('-fecha_hora')
    estado_filter = request.GET.get('estado')
    
    if estado_filter:
        turnos = turnos.filter(estado=estado_filter)
    
    return render(request, 'pacientes/listar_turnos.html', {
        'turnos': turnos,
        'estado_filter': estado_filter
    })
