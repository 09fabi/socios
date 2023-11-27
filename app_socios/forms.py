from django import forms
from .models import Socio


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'fecha_incorporacion', 'ano_nacimiento',
                  'telefono', 'correo_electronico', 'sexo', 'estado', 'observacion']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_incorporacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ano_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{9}', 'title': 'Ingrese un número telefónico válido (9 dígitos)'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}, choices=[('M', 'Masculino'), ('F', 'Femenino')]),
            'estado': forms.Select(attrs={'class': 'form-control'}, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('pendiente', 'Pendiente')]),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre': 'Nombre Del Socio',
            'fecha_incorporacion': 'Fecha De Incorporación',
            'ano_nacimiento': 'Año De Nacimiento',
            'telefono': 'Telefono',
            'correo_electronico': 'Email',
            'sexo': 'Sexo',
            'estado': 'Estado',
            'observacion': 'Observación',
        }

# Validacion para que el campo observación no sea obligatorio.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
        self.fields['observacion'].required = False

# Validacion para que el campo nombre no supere los 80 caracteres.

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) > 80:
            raise forms.ValidationError(
                "El nombre no puede superar los 80 caracteres.")
        return nombre

# Validacion para el campo correo electronico.

    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data['correo_electronico']
        return correo_electronico
