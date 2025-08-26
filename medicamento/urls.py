from django.urls import path

from medicamento.views import MedicamentoCreateView, EntradaMedicamentoCreateView, EntradaMedicamentoListView, EntradaMedicamentoDeleteView, EntradaMedicamentoUpdateView

urlpatterns = [

    path('cadastro/medicamento', MedicamentoCreateView.as_view(), name='cadastro_medicamento'),
    path('entrada/', EntradaMedicamentoCreateView.as_view(), name='entrada_medicamento_create'),
    path('estoque/', EntradaMedicamentoListView.as_view(), name='medicamento_estoque'),
    path('editar/<int:pk>/', EntradaMedicamentoUpdateView.as_view(), name='editar_medicamento'),
    path('excluir/<int:pk>/', EntradaMedicamentoDeleteView.as_view(), name='excluir_medicamento'),
]