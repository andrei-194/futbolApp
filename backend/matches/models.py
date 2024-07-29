from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from teams.models import Jugador, Equipo, Posicion
from reservations.models import Cancha


class Partido(models.Model):
    equipo_local = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cancha = models.ForeignKey(
        Cancha, on_delete=models.CASCADE, related_name='partidos')
    jugadores = models.ManyToManyField(Jugador, through='Participacion')

    def __str__(self):
        return f'{self.equipo_local} vs {self.equipo_visitante} el {self.fecha}'

    def obtener_resultado(self):
        goles_local = sum(participacion.goles for participacion in self.participacion_set.filter(
            equipo=self.equipo_local))
        goles_visitante = sum(participacion.goles for participacion in self.participacion_set.filter(
            equipo=self.equipo_visitante))
        return f'{self.equipo_local.nombre} {goles_local} - {goles_visitante} {self.equipo_visitante.nombre}'

    def clean(self):
        if self.equipo_local == self.equipo_visitante:
            raise ValidationError(
                'El mismo equipo no puede enfrentarse a sí mismo.')

    def save(self, *args, **kwargs):
        self.clean()
        super(Partido, self).save(*args, **kwargs)


class Participacion(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    goles = models.PositiveIntegerField(default=0)
    asistencias = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('partido', 'jugador')

    def __str__(self):
        return f'{self.jugador} en {self.partido}'


@receiver(post_save, sender=Participacion)
@receiver(post_delete, sender=Participacion)
def actualizar_totales_jugador(sender, instance, **kwargs):
    jugador = instance.jugador
    participaciones = Participacion.objects.filter(jugador=jugador)
    total_goles = sum(p.goles for p in participaciones)
    total_asistencias = sum(p.asistencias for p in participaciones)
    jugador.goles = total_goles
    jugador.asistencias = total_asistencias
    jugador.save()
