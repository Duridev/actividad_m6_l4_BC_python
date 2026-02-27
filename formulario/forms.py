from django import forms
from .models import ConsultaContacto

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    correo = forms.EmailField(label="Correo Electrónico")
    mensaje = forms.CharField(
        widget=forms.Textarea,
        min_length=10,
        label="Mensaje"
    )
    
    
class ConsultaContactoForm(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ['nombre', 'correo', 'mensaje']