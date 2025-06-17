from django.urls import path
from .views import PaginaView

urlpatterns = [
    path('', PaginaView.as_view(), name='pagina_index'),
]