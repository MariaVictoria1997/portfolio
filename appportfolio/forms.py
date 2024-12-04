from django import forms
from .models import Tarea, Estado

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tarea', 'fecha', 'estado']  # Campos que quieres mostrar en el formulario
