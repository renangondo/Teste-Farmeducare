from django.urls import path

from medicamento.views import EntradaMedicamentoCreateView, EstoqueView, MedicamentoListView, SaidaMedicamentoCreateView

urlpatterns = [

    path('estoque/', EstoqueView.as_view(), name='estoque_medicamento'),

    path('entrada/', EntradaMedicamentoCreateView.as_view(), name='entrada_medicamento_create'),
    path('saida/', SaidaMedicamentoCreateView.as_view(), name='saida_medicamento_create'),

    path('lista/', MedicamentoListView.as_view(), name='medicamento_list'),
]