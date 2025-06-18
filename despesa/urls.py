from django.urls import path
from .views import CategoriaDepesaCreateView, CategoriaDespesaDeleteView, CategoriaDespesaListView, CategoriaDespesaUpdateView, DespesaCreateView, DespesaDeleteView, DespesaListView, DespesaUpdateView, ParcelaDespesaCreateView, ParcelaDespesaDeleteView, ParcelaDespesaListView, ParcelaDespesaUpdateView

urlpatterns = [
    path('cadastrar/despesa', DespesaCreateView.as_view(), name='cadastrar-despesa'),
    path('cadastrar/despesa/parcelas', ParcelaDespesaCreateView.as_view(), name='cadastrar-parcela-despesa'),
    path('cadastrar/categoria/despesa', CategoriaDepesaCreateView.as_view(), name='cadastrar-categoria-despesa'),


    path('editar/despesa/<int:pk>/', DespesaUpdateView.as_view(), name='editar-despesa'),
    path('editar/despesa/parcelas/<int:pk>/', ParcelaDespesaUpdateView.as_view(), name='editar-despesa-parcelas'),
    path('editar/categoria/despesa/<int:pk>/', CategoriaDespesaUpdateView.as_view(), name='editar-categoria-despesa'),


    path('excluir/despesa/<int:pk>/', DespesaDeleteView.as_view(), name='excluir-despesa'),
    path('excluir/despesa/parcelas/<int:pk>/', ParcelaDespesaDeleteView.as_view(), name='excluir-despesa-parcelas'),
    path('excluir/categoria/despesa/<int:pk>/', CategoriaDespesaDeleteView.as_view(), name='excluir-despesa'),


    path('listar/despesa/', DespesaListView.as_view(), name='listar-despesa'),
    path('listar/despesa/parcela', ParcelaDespesaListView.as_view(), name='listar-parcela-despesa'),
    path('listar/categoria/despesa', CategoriaDespesaListView.as_view(), name='listar-categoria-despesa'),
]