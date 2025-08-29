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
        'Albahca':{
            'tipo':'hoja',
            'descripcion':'Prefiere climas calidos, no tolerancia a las heladas',
            'siembra':'Septiembre - Noviembre',
            'cosecha':'Noviembre - Enero'
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