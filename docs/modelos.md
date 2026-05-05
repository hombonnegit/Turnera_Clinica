# Modelos de Datos - Clínica de Turnos

## Diagrama de Clases

```
Usuario (Django Auth)
├── is_staff: Boolean
├── is_superuser: Boolean
└── groups: ManyToMany

Paciente
├── usuario: OneToOne -> Usuario
├── dni: CharField (unique)
├── fecha_nacimiento: DateField
├── telefono: CharField
├── obra_social: CharField
└── created_at: DateTimeField

Especialidad
├── nombre: CharField (unique)
└── descripcion: TextField

Medico
├── usuario: OneToOne -> Usuario
├── especialidad: ForeignKey -> Especialidad
├── matricula: CharField (unique)
├── telefono: CharField
├── disponible: BooleanField
└── created_at: DateTimeField

Turno
├── paciente: ForeignKey -> Paciente
├── medico: ForeignKey -> Medico
├── fecha_hora: DateTimeField
├── estado: CharField (reservado/confirmado/atendido/cancelado)
├── notas: TextField
├── created_at: DateTimeField
└── updated_at: DateTimeField

Notificacion
├── turno: ForeignKey -> Turno
├── tipo: CharField (recordatorio/confirmacion/cancelacion)
├── mensaje: TextField
├── enviada: BooleanField
├── fecha_envio: DateTimeField
└── created_at: DateTimeField
```

## Relaciones

### OneToOne
- Usuario -> Paciente
- Usuario -> Medico

### ForeignKey
- Medico -> Especialidad
- Turno -> Paciente
- Turno -> Medico
- Notificacion -> Turno

### ManyToMany
- Usuario -> Groups (Django Auth)

## Estados de Turno
- **Reservado**: Turno solicitado, pendiente de confirmación
- **Confirmado**: Turno aprobado por el médico/recepcionista
- **Atendido**: Turno completado
- **Cancelado**: Turno cancelado por paciente o sistema

## Validaciones
- DNI único por paciente
- Matrícula única por médico
- No permitir turnos en el pasado
- Un médico no puede tener múltiples turnos simultáneos
- Validar formato de teléfono y email