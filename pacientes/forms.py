from django import forms
from core.models import Paciente, Turno
from datetime import datetime, timedelta


class PacienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha de Nacimiento'
    )
    
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento', 'telefono', 'email', 'obra_social']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0',
                'placeholder': 'Nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0',
                'placeholder': 'Apellido'
            }),
            'dni': forms.TextInput(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0',
                'placeholder': 'DNI (sin puntos)',
                'maxlength': '10'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0',
                'placeholder': '+54 9 11 XXXX-XXXX',
                'type': 'tel'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0',
                'placeholder': 'correo@example.com'
            }),
            'obra_social': forms.TextInput(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0',
                'placeholder': 'Ej: OSDE, MEDIFÉ (opcional)'
            }),
        }


class TurnoForm(forms.ModelForm):
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0'
        }),
        label='Fecha y hora del turno'
    )
    
    class Meta:
        model = Turno
        fields = ['paciente', 'medico', 'fecha_hora', 'notas']
        widgets = {
            'paciente': forms.Select(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0'
            }),
            'medico': forms.Select(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0'
            }),
            'notas': forms.Textarea(attrs={
                'class': 'w-full p-3 border-2 border-gray-200 rounded-lg focus:border-indigo-500 focus:ring-0',
                'placeholder': 'Notas adicionales (síntomas, alergias, etc)',
                'rows': 3
            }),
        }
