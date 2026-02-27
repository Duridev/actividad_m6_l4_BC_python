from django import forms

class ContactForm(forms.form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    correo = forms.EmailField(label="Correo Electrónico")
    mensaje = forms.CharField(
        widget=forms.Textarea,
        min_length=10,
        label="Mensaje"
    )