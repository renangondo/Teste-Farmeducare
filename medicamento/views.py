from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from medicamento.models import EntradaMedicamento, Medicamento


############ Create Medicamento ############
class MedicamentoCreateView(LoginRequiredMixin, CreateView):
    model = Medicamento
    fields = ["nome", "fazenda"]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("pagina_index")
    extra_context = {
        "title": "Cadastro de Medicamentos",
        "titulo": "Cadastro de Medicamentos",
        "subtitulo": "Registre novos medicamentos no estoque da fazenda.",
    }


############ Create EntradaMedicamento ############
class EntradaMedicamentoCreateView(LoginRequiredMixin, CreateView):
    model = EntradaMedicamento
    fields = ["medicamento", "valor_medicamento", "quantidade", "validade", "cadastrada_por", "observacao"]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("medicamento_estoque")
    extra_context = {
        "title": "Cadastro de Entrada de Medicamentos",
        "titulo": "Cadastro de Entrada de Medicamentos",
        "subtitulo": "Registre a entrada de medicamentos no estoque da fazenda.",
    }



############ Update EntradaMedicamento ############
class EntradaMedicamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = EntradaMedicamento
    fields = ["medicamento", "valor_medicamento", "quantidade", "validade", "cadastrada_por", "observacao"]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("medicamento_estoque")
    extra_context = {
        "title": "Atualização de Entrada de Medicamentos",
        "titulo": "Atualização de Entrada de Medicamentos",
        "subtitulo": "Atualize os dados da entrada de medicamentos no estoque da fazenda.",
    }


############ Delete EntradaMedicamento ############
class EntradaMedicamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = EntradaMedicamento
    template_name = 'formularios/formulario_excluir.html'
    success_url = reverse_lazy("medicamento_estoque")
    extra_context = {
        "titulo": "Confirmação de Exclusão",
    }


############ List EntradaMedicamento ############
class EntradaMedicamentoListView(LoginRequiredMixin, ListView):
    model = EntradaMedicamento
    template_name = "medicamento_estoque.html"
    extra_context = {
        "title": "Lista de Entradas de Medicamentos",
        "titulo": "Entradas de Medicamentos",
        "registros": "Nenhuma entrada de medicamento encontrada.",
        "subtitulo": "Visualize todas as entradas de medicamentos registradas.",
        "btn_cadastrar":  "Nova Entrada"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calcula os totais
        total_quantidade = 0
        total_valor = 0
        
        for entrada in context['object_list']:
            total_quantidade += entrada.quantidade
            total_valor += entrada.valor_medicamento
        
        context['total_quantidade'] = total_quantidade
        context['total_valor'] = total_valor
        
        return context
