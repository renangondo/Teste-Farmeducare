from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Fazenda, Parceiros

# Create your views here.

class ParceirosCreateView(CreateView):
    model = Parceiros
    fields = ['nome', 'telefone', 'if_adicionais', 'email']
    template_name = 'formulario_modelo.html'
    success_url = reverse_lazy('pagina_index')

class FazendaCreateView(CreateView):
    model = Fazenda
    fields = ['usuarios', 'nome', 'descricao', 'cidade']
    template_name = 'formulario_modelo.html'
    success_url = reverse_lazy('pagina_index') 



