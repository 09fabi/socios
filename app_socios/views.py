from django.shortcuts import render, redirect, get_object_or_404
from app_socios.models import Socio
from app_socios.forms import SocioForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def listado(request):
    soc = Socio.objects.all()
    data = {'socio': soc}
    return render(request, 'listado.html', data)


def agregar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')
    else:
        form = SocioForm()
    return render(request, 'form_socio.html', {'form': form})


def eliminar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.delete()
    return redirect('listado')


def actualizar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)

    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('listado')
    else:
        form = SocioForm(instance=socio)

    return render(request, 'actualizar.html', {'form': form})
