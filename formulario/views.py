from django.shortcuts import render
from .forms import ContactForm

def formulario_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            correo = form.cleaned_data["correo"]
            mensaje = form.cleaned_data["mensaje"]
            
            return render(request, "formulario/exito.html", {"nombre": nombre})
    else:
        form = ContactForm()
    
    return render(request, "formulario/formulario.html", {"form": form})

