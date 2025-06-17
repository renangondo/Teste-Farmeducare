from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Receita, ParcelaReceita, Categoria

from django.urls import reverse_lazy

# Create your views here.


# Parte de Create View
class PaginaReceitaView(TemplateView):
    template_name = 'pagina_receita.html'

class ReceitaCreateView(CreateView):
    model = Receita
    fields = ['cliente_fornecedor', 'categoria', 'valor_total', 'parcelas', 'itens_da_receita', 'data_receita', 'fazenda_destino', 'cadastrado_por', 'observacoes', 'documento']
    template_name = 'pagina_receita.html'
    success_url = reverse_lazy('pagina_index')

class ParcelaReceitaCreateView(CreateView):
    model = ParcelaReceita
    fields = ['receita', 'ordem_parcela', 'valor_parcela', 'data_vencimento', 'valor_pago', 'status_pagamento']
    template_name = 'pagina_receita.html'
    success_url = reverse_lazy('pagina_index')
    

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'pagina_receita.html'
    success_url = reverse_lazy('pagina_index')


# Parte de Update View
class ReceitaUpdateView(UpdateView):
    model = Receita
    fields = ['cliente_fornecedor', 'categoria', 'valor_total', 'parcelas', 'itens_da_receita', 'data_receita', 'fazenda_destino', 'cadastrado_por', 'observacoes', 'documento']    
    template_name = 'pagina_receita.html'
    success_url = reverse_lazy('pagina_index')

class ParcelaReceitaUpdateView(UpdateView):
    model = ParcelaReceita
    fields = ['receita', 'ordem_parcela', 'valor_parcela', 'data_vencimento', 'valor_pago', 'status_pagamento']
    template_name = 'pagina_receita.html'
    success_url = reverse_lazy('pagina_index')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'pagina_receita.html'
    success_url = reverse_lazy('pagina_index')


#Parte de Delete View
class ReceitaDeleteView(DeleteView):
    model = Receita
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('pagina_index')


class ParcelaReceitaDeleteView(DeleteView):
    model = ParcelaReceita
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('pagina_index')


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('pagina_index')

#Parte de List View
class ReceitaListView(ListView):
    model = Receita
    template_name = 'listas/receita_list.html'

class ParcelaReceitaListView(ListView):
    model = ParcelaReceita
    template_name = 'listas/parcelas_list.html'

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'listas/categoria_list.html'