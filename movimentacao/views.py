from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Categoria, Movimentacao, Parcela


# Create your views here.

############  CRUD das entidades Movimentacao, Parcela, Categoria  ############


############ Create Movimentacao ############
class MovimentacaoCreateView(CreateView):
    model = Movimentacao
    fields = [
        "tipo",
        "parceiros",
        "categoria",
        "valor_total",
        "parcelas",
        "imposto_renda",
        "descricao",
        "data",
        "fazenda",
        "cadastrada_por",
    ]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("pagina_index")
    extra_context = {
        "title": "Cadastro de Movimentações",
        "titulo": "Cadastro de Movimentações",
        "subtitulo": "Movimentações são usadas para registrar entradas e saídas de dinheiro na fazenda.",
    }


############ Create Parcela ############
class ParcelaCreateView(CreateView):
    model = Parcela
    fields = [
        "movimentacao",
        "ordem_parcela",
        "valor_parcela",
        "data_vencimento",
        "valor_pago",
        "status_pagamento",
        "data_quitacao",
    ]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("pagina_index")

    extra_context = {
        "title": "Cadastro de Parcelas",
        "titulo": "Cadastro de Parcelas",
        "subtitulo": "Parcelas são usadas para dividir o valor de uma movimentação em várias partes.",
    }


############ Create Categoria ############
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ["nome", "tipo"]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("pagina_index")

    extra_context = {
        "title": "Cadastro de Categorias",
        "titulo": "Cadastro de Categorias",
        "subtitulo": "Categorias são usadas para classificar as movimentações financeiras.",
    }


############ Update Movimentacao ############
class MovimentacaoUpdateView(UpdateView):
    model = Movimentacao
    fields = [
        "tipo",
        "parceiros",
        "categoria",
        "valor_total",
        "parcelas",
        "imposto_renda",
        "descricao",
        "data",
        "fazenda",
    ]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("pagina_index")
    extra_context = {
        "title": "Atualização de Movimentações",
        "titulo": "Atualização de Movimentações",
    }


############ Update Parcela ############
class ParcelaUpdateView(UpdateView):
    model = Parcela
    fields = [
        "movimentacao",
        "ordem_parcela",
        "valor_parcela",
        "data_vencimento",
        "valor_pago",
        "status_pagamento",
        "data_quitacao",
    ]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("pagina_index")

    extra_context = {
        "title": "Atualização de Parcelas",
        "titulo": "Atualização de Parcelas",
    }


############ Update Categoria ############
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ["nome", "tipo"]
    template_name = "formularios/formulario_modelo.html"
    success_url = reverse_lazy("pagina_index")

    extra_context = {
        "title": "Atualização de Categorias",
        "titulo": "Atualização de Categorias",
    }


############ Delete Movimentacao ############
class MovimentacaoDeleteView(DeleteView):
    model = Movimentacao
    template_name = "formularios/formulario_excluir.html"
    success_url = reverse_lazy("pagina_index")

    extra_context = {
        "title": "Exclusão de Movimentações",
        "titulo_excluir": "Exclusão de Movimentações",
    }


############ Delete Parcela ############
class ParcelaDeleteView(DeleteView):
    model = Parcela
    template_name = "formularios/formulario_excluir.html"
    success_url = reverse_lazy("pagina_index")

    extra_context = {
        "title": "Exclusão de Parcelas",
        "titulo_excluir": "Exclusão de Parcelas",
    }


############ Delete Categoria ############
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "formularios/formulario_excluir.html"
    success_url = reverse_lazy("pagina_index")

    extra_context = {
        "title": "Exclusão de Categorias",
        "titulo_excluir": "Exclusão de Categorias",
    }


############ List Movimentação Genérica ############
class MovimentacaoListView(ListView):
    model = Movimentacao
    template_name = "movimentacao/lista_movimentacoes.html"

    def get_queryset(self):
        return Movimentacao.objects.all().order_by("-data")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["despesas"] = Movimentacao.objects.filter(tipo="despesa")
        context["receitas"] = Movimentacao.objects.filter(tipo="receita")
        return context

    extra_context = {
        "title": "Lista de Movimentações",
        "titulo": "Movimentações",
        "subtitulo": "Aqui você pode visualizar todas as movimentações financeiras registradas.",
        "registros": "Nenhum registro encontrado.",
    }


############ List Movimentação Receita ############
class MovimentacaoReceitaListView(ListView):
    model = Movimentacao
    template_name = "receita/lista_receita.html"

    def get_queryset(self):
        return Movimentacao.objects.filter(tipo="receita").order_by("-data")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calcula os totais para receitas
        total_receitas = 0
        for receita in context["object_list"]:
            total_receitas += receita.valor_total

        context["total_receitas"] = total_receitas

        return context

    extra_context = {
        "title": "Lista de Receitas",
        "titulo": "Receitas",
        "subtitulo": "Aqui você pode visualizar todas as receitas registradas.",
        "registros": "Nenhuma receita encontrada.",
        "btn_cadastrar": "Nova Receita",
    }


############ List Movimentação Despesa ############
class MovimentacaoDespesaListView(ListView):
    model = Movimentacao
    template_name = "despesa/lista_despesa.html"

    def get_queryset(self):
        return Movimentacao.objects.filter(tipo="despesa").order_by("-data")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calcula os totais para despesas
        total_despesas = 0
        for despesa in context["object_list"]:
            total_despesas += despesa.valor_total

        context["total_despesas"] = total_despesas

        return context

    extra_context = {
        "title": "Lista de Despesas",
        "titulo": "Despesas",
        "subtitulo": "Aqui você pode visualizar todas as despesas registradas.",
        "registros": "Nenhuma despesa encontrada.",
        "btn_cadastrar": "Nova Despesa",
    }

