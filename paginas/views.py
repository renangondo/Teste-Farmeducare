from datetime import datetime, timedelta
from django.views.generic import TemplateView
from django.db.models import Sum
from movimentacao.models import Movimentacao
from medicamento.models import EntradaMedicamento
import json


class PaginaView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Total de receitas
        total_receitas = (
            Movimentacao.objects.filter(tipo="receita").aggregate(
                total=Sum("valor_total")
            )["total"]
            or 0
        )

        # Total de despesas
        total_despesas = (
            Movimentacao.objects.filter(tipo="despesa").aggregate(
                total=Sum("valor_total")
            )["total"]
            or 0
        )

        # Saldo (receitas - despesas)
        saldo = total_receitas - total_despesas

        # Buscar as entradas de medicamentos
        entradas_medicamentos = EntradaMedicamento.objects.select_related(
            "medicamento"
        ).all()
        context["entradas_medicamentos"] = entradas_medicamentos

        total_quantidade = 0
        total_valor = 0

        for entrada in entradas_medicamentos:
            total_quantidade += entrada.quantidade
            total_valor += entrada.valor_medicamento

        context["total_quantidade"] = total_quantidade
        context["total_valor"] = total_valor
        context["total_receitas"] = total_receitas
        context["total_despesas"] = total_despesas
        context["saldo"] = saldo

        # Dados para os gráficos
        grafico_linhas = self.get_dados_grafico_linhas()
        grafico_pizza = self.get_dados_grafico_pizza()

        context["grafico_receitas_despesas"] = grafico_linhas
        context["grafico_categorias"] = grafico_pizza

        # Passar dados para JavaScript (serializados como JSON)
        context["grafico_data_json"] = json.dumps(
            {
                "meses": grafico_linhas["meses"],
                "receitas": grafico_linhas["receitas"],
                "despesas": grafico_linhas["despesas"],
                "categorias": grafico_pizza["categorias"],
                "valores": grafico_pizza["valores"],
                "totais": {
                    "receitas": float(total_receitas),
                    "despesas": float(total_despesas),
                    "saldo": float(saldo),
                },
            }
        )

        return context

    def get_dados_grafico_linhas(self):
        # Dados dos últimos 6 meses
        meses = []
        receitas_mensais = []
        despesas_mensais = []

        for i in range(5, -1, -1):  # Últimos 6 meses em ordem cronológica
            mes = (datetime.now() - timedelta(days=30 * i)).strftime("%Y-%m")
            meses.append(mes)

            receitas = (
                Movimentacao.objects.filter(
                    tipo="receita", data__startswith=mes
                ).aggregate(total=Sum("valor_total"))["total"]
                or 0
            )

            despesas = (
                Movimentacao.objects.filter(
                    tipo="despesa", data__startswith=mes
                ).aggregate(total=Sum("valor_total"))["total"]
                or 0
            )

            receitas_mensais.append(float(receitas))
            despesas_mensais.append(float(despesas))

        return {
            "meses": meses,
            "receitas": receitas_mensais,
            "despesas": despesas_mensais,
        }

    def get_dados_grafico_pizza(self):
        # Distribuição de despesas por categoria
        categorias = (
            Movimentacao.objects.filter(tipo="despesa")
            .values("categoria__nome")
            .annotate(total=Sum("valor_total"))
            .order_by("-total")
        )

        # Se não houver dados, retornar valores vazios
        if not categorias:
            return {"categorias": [], "valores": []}

        return {
            "categorias": [
                cat["categoria__nome"] or "Sem Categoria" for cat in categorias
            ],
            "valores": [float(cat["total"] or 0) for cat in categorias],
        }
