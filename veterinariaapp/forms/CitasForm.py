from django import forms
from veterinariaapp.models.Citas import Citas
from veterinariaapp.models.Usuarios import Usuarios
from veterinariaapp.models.Servicios import Servicios
from veterinariaapp.models.Mascotas import Mascotas

class CitasForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=Usuarios.objects.filter(status=1).order_by('usuario')
    )

    id_mascota = forms.ModelChoiceField(
        queryset=Mascotas.objects.order_by('nombre')
    )

    id_servicio = forms.ModelChoiceField(
        queryset=Servicios.objects.order_by('nombre')
    )

    class Meta:
        model = Citas
        fields = ('id_cita','id_servicio','fecha','id_mascota','usuario')
        widgets={

            'fecha': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'input-form3'})
        }

    def __init__(self, *args, **kwargs):
        super(CitasForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['class'] = 'input-form'
        self.fields['id_mascota'].widget.attrs['class'] = 'input-form'
        self.fields['id_servicio'].widget.attrs['class'] = 'input-form'