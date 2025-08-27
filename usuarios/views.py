from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UsuarioCadastroForm

class CadastroUsuarioView(CreateView):
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Adiciona ao grupo Funcionario
        grupo, criado = Group.objects.get_or_create(name='Funcionario')
        self.object.groups.add(grupo)
        
        # Define que o usuário está ativo
        self.object.is_active = True
        self.object.save()
        
        messages.success(
            self.request,
            'Conta criada com sucesso! Agora você pode fazer login.'
        )
        
        return response

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija os erros abaixo.'
        )
        return super().form_invalid(form)