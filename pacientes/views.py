from django.shortcuts import render
from django.http import JsonResponse
from core.models import Medico, Especialidad


def sacar_turno(request):
    """Renderiza el formulario de reserva de turnos"""
    return render(request, 'pacientes/sacar_turno.html')


def buscar_medicos(request):
    """Busca médicos por especialidad vía AJAX/HTMX"""
    especialidad_id = request.GET.get('especialidad')

    if not especialidad_id:
        return JsonResponse({'error': 'Especialidad no proporcionada'}, status=400)

    medicos = Medico.objects.filter(especialidad_id=especialidad_id, disponible=True)

    html = '<select name="medico" class="w-full p-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-indigo-500">'
    for medico in medicos:
        html += f'<option value="{medico.id}">{medico.nombre}</option>'
    html += '</select>'

    return JsonResponse({'html': html})
