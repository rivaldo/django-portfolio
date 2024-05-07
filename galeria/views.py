from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia





def index(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards':fotografias})

def imagem(request):
    fotografia = get_object_or_404()
    return render(request, 'galeria/imagem.html', {'fotografia':fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] #GET Corrigido aqui!!
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})
