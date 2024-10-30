from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            'nombre_servicio',
            'categoria',
            'subcategoria',
            'precio_anterior',
            'descuento',
            'precio_oferta_actual',
            'estado',
        ]
        widgets = {
            'estado': forms.Select(),
        }
