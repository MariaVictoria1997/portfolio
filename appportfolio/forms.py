from django import forms
from .models import Tarea, Estado, Proyecto
################################################
# TAREAS
################################################
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tarea', 'fecha', 'estado']  # Campos que quieres mostrar en el formulario
################################################
# PROYECTOS
################################################
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'lenguaje', 'tecnologias', 'observaciones', 'fecha_publicacion']