from django import forms
from veterinariaapp.models.Productos import Productos

class ProductosForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ('referencia','descripcion','marca','precio','imagen')
        widgets={
            'referencia': forms.TextInput(attrs={'class': 'input-form'}),
            'descripcion': forms.TextInput(attrs={'class': 'input-form'}),
            'precio': forms.NumberInput(attrs={'class': 'input-form'}),
            'marca': forms.TextInput(attrs={'class': 'input-form'}),
            'imagen': forms.TextInput(attrs={'class': 'input-form'}),

        }