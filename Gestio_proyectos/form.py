from django.forms import ModelForm
from .models import Proyecto,Equipo,Tarea

class ProyectoForm(ModelForm):
    class Meta:
        model= Proyecto
        fields = ['nombre','equipo']
        

class EquipoForm(ModelForm):
    class Meta:
        model= Equipo
        fields = ['nombre','usuarios']
        
class TareaForm(ModelForm):
    class Meta:
        model= Tarea
        fields = ['nombre','fecha_inicio','fecha_fin','responsable','ejecutor','proyecto']
        
        
     