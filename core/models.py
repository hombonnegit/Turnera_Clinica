from django.db import models


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"


class Medico(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    matricula = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad.nombre})"

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"


class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    obra_social = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Turno(models.Model):
    ESTADOS = [
        ('reservado', 'Reservado'),
        ('confirmado', 'Confirmado'),
        ('atendido', 'Atendido'),
        ('cancelado', 'Cancelado'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='reservado')
    notas = models.TextField(blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Turno: {self.paciente} con {self.medico.nombre} - {self.fecha_hora}"

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        ordering = ['fecha_hora']