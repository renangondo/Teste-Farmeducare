from django.urls import path
from .views import ReceitaCreateView, ParcelaReceitaCreateView, CategoriaCreateView
from .views import ReceitaUpdateView, ParcelaReceitaUpdateView, CategoriaUpdateView
from .views import ReceitaDeleteView, ParcelaReceitaDeleteView, CategoriaDeleteView
from .views import ReceitaListView, ParcelaReceitaListView, CategoriaListView


urlpatterns = [
      path('cadastrar/receita', ReceitaCreateView.as_view(), name='cadastrar-receita'),
      path('cadastrar/receita/parcelas', ParcelaReceitaCreateView.as_view(), name='cadastrar-parcela-receita'),
      path('cadastrar/categoria', CategoriaCreateView.as_view(), name='cadastrar-categoria'),


      path('editar/receita/<int:pk>/', ReceitaUpdateView.as_view(), name='editar-receita'),
      path('editar/receita/parcelas/<int:pk>/', ParcelaReceitaUpdateView.as_view(), name='editar-receita-parcelas'),
      path('editar/categoria/<int:pk>/', CategoriaUpdateView.as_view(), name='editar-categoria'),


      path('excluir/receita/<int:pk>/', ReceitaDeleteView.as_view(), name='excluir-receita'),
      path('excluir/receita/parcelas/<int:pk>/', ParcelaReceitaDeleteView.as_view(), name='excluir-receita-parcelas'),
      path('excluir/categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='excluir-categoria'),


      path('listar/receita/', ReceitaListView.as_view(), name='listar-receita'),
      path('listar/receita/parcela', ParcelaReceitaListView.as_view(), name='listar-parcela'),
      path('listar/categoria/', CategoriaListView.as_view(), name='listar-categoria'),
]