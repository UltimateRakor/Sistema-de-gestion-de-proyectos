
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    usuarios = models.ManyToManyField(User, related_name='equipos')

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='proyectos')

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_responsable')
    ejecutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_ejecutor')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
