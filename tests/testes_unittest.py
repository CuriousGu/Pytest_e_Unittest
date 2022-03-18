from unittest import TestCase
from main.user import Pessoa, Leilao


class TestLeilao(TestCase):
    def setUp(self):
        self.leilao = Leilao('computador', 100)
        self.gu = Pessoa('Gustavo', 150)
        self.vilma = Pessoa('Vilma', 300)

    def test_deve_retornar_o_saldo_atualizado_apos_adicionar_alguma_quantia(self):
        self.gu.adiciona_saldo(150)
        self.assertEqual(300, self.gu.saldo)

    def test_deve_recusar_lance_inferior_ao_lance_minimo(self):
        try:
            self.gu.dar_lance(50, self.leilao)

        except ValueError:
            self.assertEqual(len(self.leilao.lista_lances), 1)

    def test_deve_recursar_lance_maior_que_saldo(self):
        pass
