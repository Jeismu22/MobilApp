from django import forms
from .models import Carpeta, Proyecto, Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'fecha_limite', 'estado']  # Asegúrate de incluir el campo 'estado'
        widgets = {
            'estado': forms.RadioSelect(choices=Tarea.ESTADO_CHOICES)  # Usar un select para elegir el estado
        }

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'fecha_limite', 'estado']
        widgets = {
            'estado': forms.RadioSelect(choices=Proyecto.ESTADO_CHOICES)
        }

class CarpetaForm(forms.ModelForm):
    class Meta:
        model = Carpeta
        fields = ['titulo', 'estado']
        widgets = {
            'estado': forms.RadioSelect(choices=Carpeta.ESTADO_CHOICES)
        }