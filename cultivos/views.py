from django.shortcuts import render, redirect
from .forms import CultivoForm
from .models import Cultivo

def registrar_cultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cultivos')
    else:
        form = CultivoForm()
    return render(request, 'cultivos/registrar_cultivos.html', {'form': form})

def listar_cultivos(request):
    cultivos = Cultivo.objects.all()
    return render(request, 'cultivos/lista_cultivos.html', {
        'titulo': 'listado de cultivos',
        'cultivos': cultivos    
        })
    


def detalle_cultivo(request, nombre):
    pass



def recomendar_cultivos(request):
    estacion = request.GET.get('estacion', '')
    estaciones = {
        'primavera': 
            {'Lechuga', 'Cilantro'},
        'verano': 
            {'Pimiento', 'Albahaca'},
        'otoño': 
            {'Tomate', 'Albahaca', 'Zanahoria'},
        'invierno': 
            {'Zanahoria', 'Tomate'},
    }
    cultivos_recomendados = estaciones.get(estacion, [])
    contexto = {
        'estacion': estacion,
        'cultivos_recomendados': cultivos_recomendados,
    }
    return render(request, 'cultivos/recomendacion.html', contexto)