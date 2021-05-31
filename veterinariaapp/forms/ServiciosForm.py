from django import forms
from veterinariaapp.models.Servicios import Servicios

class ServiciosForm(forms.ModelForm):

    class Meta:
        model = Servicios
        fields = ('nombre','precioxservicio','descripcion','imagen')
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'input-form'}),
            'precioxservicio': forms.NumberInput(attrs={'class': 'input-form'}),
            'descripcion': forms.TextInput(attrs={'class': 'input-form'}),
            'imagen': forms.TextInput(attrs={'class': 'input-form'}),

        }