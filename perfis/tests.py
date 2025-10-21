from django.test import TestCase 
from django.contrib.auth.models import User
from .models import Fazenda, Parceiros


class FazendaModelTest(TestCase):
    
    def test_criar_fazenda(self):
        fazenda = Fazenda.objects.create(
            nome='Fazenda São João',
            cidade='Ribeirão Preto',
            descricao='Fazenda especializada em gado leiteiro'
        )
        
        self.assertEqual(fazenda.nome, 'Fazenda São João')
        self.assertEqual(fazenda.cidade, 'Ribeirão Preto')
        self.assertEqual(str(fazenda), 'Fazenda São João - Ribeirão Preto')


class ParceirosModelTest(TestCase):
    
    def test_criar_parceiro(self):

        parceiro = Parceiros.objects.create(
            nome='Agropecuária Silva',
            telefone='(16) 99999-9999',
            email='contato@agropecuariasilva.com'
        )
        
        self.assertEqual(parceiro.nome, 'Agropecuária Silva')
        self.assertEqual(parceiro.telefone, '(16) 99999-9999')
        self.assertEqual(str(parceiro), 'Agropecuária Silva')


class RelacionamentoTest(TestCase):
    """Teste para relacionamento entre Usuário e Fazenda"""
    
    def test_usuario_fazenda_relacionamento(self):
        """Testa o relacionamento ManyToMany entre Usuário e Fazenda"""
        # Criar usuário
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Criar fazenda
        fazenda = Fazenda.objects.create(
            nome='Fazenda Teste',
            cidade='São Paulo'
        )
        
        # Associar usuário à fazenda
        fazenda.usuarios.add(user)
        
        # Verificar relacionamento
        self.assertEqual(fazenda.usuarios.count(), 1)
        self.assertTrue(fazenda.usuarios.filter(username='testuser').exists())
