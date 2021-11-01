from django.shortcuts import render

# Create your views here.
from ofertas.models import Supermercado, Produto, Em_Oferta

def index(request):
    """Função view para a página inicial do site"""
    #Gera alguns contadores para os objetos principais
    num_super = Supermercado.objects.all().count()
    num_prod = Produto.objects.all().count()
    num_ofertas = Em_Oferta.objects.all().count()
    
    
    context = {
        'num_super': num_super,
        'num_prod': num_prod,
        'num_ofertas': num_ofertas,
    }
    
    #Renderiza o template index.html com os dados na variável context
    return render(request, 'index.html', context=context)

def about(request):
    """Função view para a página sobre nós do site"""
      #Renderiza o template about.html
    return render(request, 'about.html')

from django.views import generic

class SupermercadoListView(generic.ListView):
    model = Supermercado

class ProdutoListView(generic.ListView):
    model = Produto

class Em_OfertaListView(generic.ListView):
    model = Em_Oferta
 
def ofertasporsuper(request, pk):
    """Função view para a página ofertas por super"""
    ofertasporsuper = Em_Oferta.objects.filter(sm__id__exact=pk)
    nomesuper = ofertasporsuper[0].sm
    
    
    context = {
        'ofertasporsuper': ofertasporsuper,
        'nomesuper': nomesuper,
    }
    
    #Renderiza o template index.html com os dados na variável context
    return render(request, 'ofertasporsuper.html', context=context)
    
def ondeencontrar(request, pk):
    """Função view para a encontrar supermercados que possuem um produto específico em oferta"""
    locais = Em_Oferta.objects.filter(pd__id__exact=pk)
    produto = locais[0].pd
    
    
    context = {
        'locais': locais,
        'produto': produto,
    }
    
    #Renderiza o template ondeencontrar.html com os dados na variável context
    return render(request, 'ondeencontrar.html', context=context)
