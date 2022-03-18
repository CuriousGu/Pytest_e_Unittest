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
        with self.assertRaises(ValueError):
            self.gu.dar_lance(50, self.leilao)

    def test_deve_descontar_o_valor_do_lance_do_saldo(self):
        self.gu.dar_lance(140, self.leilao)
        self.assertEqual(self.gu.saldo, 10)

    def test_deve_recursar_lance_maior_que_saldo(self):
        with self.assertRaises(ValueError):
            self.gu.dar_lance(200, self.leilao)

    def test_deve_contabilizar_dois_lances_validos(self):
        self.vilma.dar_lance(100, self.leilao)
        self.gu.dar_lance(150, self.leilao)

        self.assertEqual(len(self.leilao.lista_lances) - 1, 2)

    def test_deve_aceitar_primeiro_lance_se_for_de_mesmo_valor_que_o__lance_minimo(self):
        self.vilma.dar_lance(100, self.leilao)

        self.assertEqual(len(self.leilao.lista_lances), 2)

    def test_deve_recusar_lance_se_for_de_mesmo_valor_que_o_lance_anterior(self):
        self.vilma.dar_lance(100, self.leilao)

        try:
            self.gu.dar_lance(100, self.leilao)
        except ValueError:
            self.assertEqual(len(self.leilao.lista_lances), 2)
