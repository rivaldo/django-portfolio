from django.shortcuts import render





def index(request):
    dados = {
        1: {
            'nome':'Nebulosa de Carina',
            'legenda':'webtelescope.org / NASA / James'
        },
        2:{
            'nome':'Galaxia NGC 1970',
            'legenda':'nasa.org / NASA / Hubble'
        }
    }
    return render(request, 'galeria/index.html', {'cards':dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')