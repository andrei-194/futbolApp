# Generated by Django 4.2.6 on 2024-07-28 04:40


from django.db import migrations

def crear_posiciones(apps, schema_editor):
    Posicion = apps.get_model('teams', 'Posicion')
    posiciones = [
        'Portero', 'Defensa Central', 'Lateral Derecho', 'Lateral Izquierdo', 
        'Mediocentro', 'Extremo Derecho', 'Extremo Izquierdo', 
        'Delantero Centro', 'Mediapunta', 'Defensa Derecho', 'Defensa Izquierdo'
    ]
    for posicion in posiciones:
        Posicion.objects.create(nombre=posicion)

class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_posiciones),
    ]

