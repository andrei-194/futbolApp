from django.db import models
from django.contrib.auth.models import User
from users.models import Perfil
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    dueño = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='equipos')
    descripcion = models.TextField(blank=True, null=True)
    fecha_fundacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Posicion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    goles = models.PositiveIntegerField(default=0)
    asistencias = models.PositiveIntegerField(default=0)
    partidos_jugados = models.PositiveIntegerField(default=0)
    pierna_habil = models.CharField(max_length=10, choices=[(
        'derecha', 'Derecha'), ('izquierda', 'Izquierda'), ('ambas', 'Ambas')], default='derecha')
    posiciones = models.ManyToManyField(Posicion, related_name='jugadores')
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.perfil.user.username
