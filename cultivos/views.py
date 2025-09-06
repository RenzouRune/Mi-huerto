from django.shortcuts import render

def listar_cultivos(request):
    cultivos_originales = [
        {'nombre': 'Tomate', 'tipo': 'fruto'},
        {'nombre': 'Lechuga', 'tipo': 'hoja'},
        {'nombre': 'Albahaca', 'tipo': 'hoja'},
        {'nombre': 'Zanahoria', 'tipo': 'raiz'},
        {'nombre': 'Cilantro', 'tipo': 'hoja'},
        {'nombre': 'Pimiento', 'tipo': 'fruto'},
        
    ]
    termino = request.GET.get('buscar','')
    tipo = request.GET.get('tipo', '')
    cultivo_filtrados = cultivos_originales

    if termino:
        cultivo_filtrados = [c for c in cultivo_filtrados if termino.lower() in c['nombre'].lower()]
    if tipo:
        cultivo_filtrados = [c for c in cultivo_filtrados if tipo.lower() in c['tipo'] == tipo]

    contexto = {
        'titulo':'Mi huerto',
        'mensaje':'Filtra los cultivos por nombre y tipo',
        'cultivos': cultivo_filtrados,
    }
    return render(request, 'cultivos/lista_cultivos.html', contexto)

def detalle_cultivo(request, nombre):
    cultivos = {
        'Tomate':{
            'tipo':'fruto',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frio',
            'siembra':'Agosto - Octubre',
            'cosecha':'Noviembre - Enero'
        },
        'Lechuga':{
            'tipo':'hoja',
            'descripcion':'Preferiblemente sombra y suelo humedo',
            'siembra':'Marzo - Mayo',
            'cosecha':'60 dias despues de ser sembrado'            
        },
        'Albahaca':{
            'tipo':'hoja',
            'descripcion':'Prefiere climas calidos, no tolerancia a las heladas',
            'siembra':'Septiembre - Noviembre',
            'cosecha':'Noviembre - Enero'
        },
        'Zanahoria':{
            'tipo':'raiz',
            'descripcion':'Prefiere climas calidos, no tolerancia a las heladas',
            'siembra':'Noviembre - Enero',
            'cosecha':'Enero - Febrero'
        },
        'Cilantro':{
            'tipo':'hoja',
            'descripcion':'Prefiere climas Frios, no tolerancia a las Calientes',
            'siembra':'Febrero - Abril',
            'cosecha':'Abril - Mayo'
        },
        'Pimiento':{
            'tipo':'fruto',
            'descripcion':'Prefiere climas calidos, no tolerancia a las heladas',
            'siembra':'Julio - Septiembre',
            'cosecha':'Septiembre - Noviembre'
        },
    }
    cultivos = cultivos.get(nombre)
    if not cultivos:
        return render(request, 'cultivos/no_encontrado.html', {'nombre': nombre})
    contexto = {
        'nombre':nombre,
        'tipo':cultivos['tipo'],
        'descripcion':cultivos['descripcion'],
        'siembra':cultivos['siembra'],
        'cosecha':cultivos['cosecha'],
    }
    return render(request, 'cultivos/detalle.html', contexto)



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