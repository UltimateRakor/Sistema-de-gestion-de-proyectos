from django.contrib import admin
from .models import Proyecto,Equipo,Tarea

# Register your models here.
admin.site.register( Proyecto)
admin.site.register( Equipo)
admin.site.register( Tarea)