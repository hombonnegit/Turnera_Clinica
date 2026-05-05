from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad.nombre})"

class Turno(models.Model):
    paciente_nombre = models.CharField(max_length=200)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Turno: {self.paciente_nombre} con {self.medico.nombre}"