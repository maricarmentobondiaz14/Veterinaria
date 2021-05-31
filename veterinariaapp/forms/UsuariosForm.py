from django import forms
from veterinariaapp.models.Usuarios import Usuarios

class UsuariosForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ('usuario','nombre','password','tipousuario','direccion','ciudad','codigopostal','telefono','correo','status')
        widgets={
            'usuario': forms.TextInput(attrs={'class': 'input-form','placeholder':'Ingrese el usuario'}),
            'nombre': forms.TextInput(attrs={'class': 'input-form','placeholder':'Ingrese un nombre'}),
            'direccion': forms.TextInput(attrs={'class':'input-form'}),
            'ciudad': forms.TextInput(attrs={'class': 'input-form'}),
            'codigopostal': forms.NumberInput(attrs={'class': 'input-form'}),
            'telefono': forms.TextInput(attrs={'class': 'input-form'}),
            'correo': forms.TextInput(attrs={'class': 'input-form'}),
        }