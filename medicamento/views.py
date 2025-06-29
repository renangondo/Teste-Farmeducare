from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from medicamento.models import EntradaMedicamento, Medicamento, SaidaMedicamento

# Create your views here.
class EstoqueView(TemplateView):
    template_name = 'medicamento_estoque.html'


class EntradaMedicamentoCreateView(CreateView):
    model = EntradaMedicamento
    fields = [
        'medicamento',
        'quantidade',
        'validade',
        'cadastrado_por'
    ]
    template_name = 'formularios/formulario_modelo.html'
    success_url = reverse_lazy('pagina_index')
    extra_context = {
        "title": "Cadastro de Entrada de Medicamentos",
        "titulo": "Cadastro de Entrada de Medicamentos",
        "subtitulo": "Registre a entrada de medicamentos no estoque da fazenda."
    }

    def form_valid (self, form):
        form.instance.cadastrado_por = self.request.user  
        url = super().form_valid(form)
        return url



class SaidaMedicamentoCreateView(CreateView):
    model = SaidaMedicamento
    fields = [
        'medicamento',
        'quantidade',
        'cadastrado_por'
    ]
    template_name = 'formularios/formulario_modelo.html'
    success_url = reverse_lazy('pagina_index')
    extra_context = {
        "title": "Cadastro de Saída de Medicamentos",
        "titulo": "Cadastro de Saída de Medicamentos",
        "subtitulo": "Registre a saída de medicamentos do estoque da fazenda."
    }

class MedicamentoCreateView(CreateView):
    model = Medicamento
    fields = [
        'nome',
        'quantidade',
        'validade',
        'fazenda'
    ]
    template_name = 'formularios/formulario_modelo.html'
    success_url = reverse_lazy('pagina_index')
    extra_context = {
        "title": "Cadastro de Medicamentos",
        "titulo": "Cadastro de Medicamentos",
        "subtitulo": "Registre novos medicamentos no estoque da fazenda."
    }




class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'medicamento/medicamento_estoque.html'
    extra_context = {
        "title": "Lista de Entradas de Medicamentos",
        "titulo": "Entradas de Medicamentos",
        "subtitulo": "Visualize todas as entradas de medicamentos registradas."
    }



