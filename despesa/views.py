from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Despesa, ParcelaDespesa, CategoriaDespesa

from django.urls import reverse_lazy

# Create your views here.

class PaginaDespesaView(TemplateView):
    template_name = 'pagina_despesa.html'

class DespesaCreateView(CreateView):
    model = Despesa
    fields = ['cliente_fornecedor', 'categoria', 'valor_total', 'parcelas', 'descricao', 'imposto_renda','data_despesa', 'fazenda_destino', 'cadastrado_por', 'cadastrado_em']
    template_name = 'pagina_despesa.html'
    success_url = reverse_lazy('pagina_index')

class ParcelaDespesaCreateView(CreateView):
    model = ParcelaDespesa
    fields = ['despesa', 'ordem_parcela', 'valor_parcela', 'data_vencimento']
    template_name = 'pagina_despesa.html'
    success_url = reverse_lazy('pagina_index')
    

class CategoriaDepesaCreateView(CreateView):
    model = CategoriaDespesa
    fields = ['nome']
    template_name = 'pagina_despesa.html'
    success_url = reverse_lazy('pagina_index')


# Parte de Update View
class DespesaUpdateView(UpdateView):
    model = Despesa
    fields = ['cliente_fornecedor', 'categoria', 'valor_total', 'parcelas', 'descricao', 'imposto_renda','data_despesa', 'fazenda_destino', 'cadastrado_por', 'cadastrado_em']  
    template_name = 'pagina_despesa.html'
    success_url = reverse_lazy('pagina_index')

class ParcelaDespesaUpdateView(UpdateView):
    model = ParcelaDespesa
    fields = ['despesa', 'ordem_parcela', 'valor_parcela', 'data_vencimento']
    template_name = 'pagina_despesa.html'
    success_url = reverse_lazy('pagina_index')

class CategoriaDespesaUpdateView(UpdateView):
    model = CategoriaDespesa
    fields = ['nome']
    template_name = 'pagina_despesa.html'
    success_url = reverse_lazy('pagina_index')


#Parte de Delete View
class DespesaDeleteView(DeleteView):
    model = Despesa
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('pagina_index')


class ParcelaDespesaDeleteView(DeleteView):
    model = ParcelaDespesa
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('pagina_index')


class CategoriaDespesaDeleteView(DeleteView):
    model = CategoriaDespesa
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('pagina_index')

#Parte de List View
class DespesaListView(ListView):
    model = Despesa
    template_name = 'listas/despesa_list.html'

class ParcelaDespesaListView(ListView):
    model = ParcelaDespesa
    template_name = 'listas/parcelas_despesa_list.html'

class CategoriaDespesaListView(ListView):
    model = CategoriaDespesa
    template_name = 'listas/categoria_despesa_list.html'