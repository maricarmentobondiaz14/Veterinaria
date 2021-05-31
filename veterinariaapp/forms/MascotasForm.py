from django import forms
from veterinariaapp.models.Mascotas import Mascotas
from veterinariaapp.models.Usuarios import Usuarios


class MascotasForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=Usuarios.objects.order_by('usuario')
    )

    class Meta:
        model = Mascotas
        fields = ('nombre','usuario','tipo_animal','raza','genero','esterilizado','longitud','peso','vacunas','imagen')
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'input-form'}),
            'tipo_animal': forms.TextInput(attrs={'class': 'input-form'}),
            'raza': forms.TextInput(attrs={'class': 'input-form'}),
            'longitud': forms.NumberInput(attrs={'class': 'input-form'}),
            'peso': forms.NumberInput(attrs={'class': 'input-form'}),
            'vacunas': forms.TextInput(attrs={'class': 'input-form'}),
            'imagen': forms.TextInput(attrs={'class': 'input-form'}),

        }

    def __init__(self, *args, **kwargs):
        super(MascotasForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['class'] = 'input-form'

