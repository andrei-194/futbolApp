from django.db import models
from django.contrib.auth.models import User
from teams.models import Equipo


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    dueño = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='canchas')
    ubicacion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField(blank=True, null=True)
    tipo_superficie = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Reservacion(models.Model):
    cancha = models.ForeignKey(
        Cancha, on_delete=models.CASCADE, related_name='reservaciones')
    equipo = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, related_name='reservaciones')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), (
        'confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], default='pendiente')

    def __str__(self):
        return f'{self.cancha} reservada por {self.equipo} el {self.fecha} de {self.hora_inicio} a {self.hora_fin}'
