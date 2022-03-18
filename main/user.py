class Pessoa:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def adiciona_saldo(self, valor):
        self.saldo += valor

    def dar_lance(self, valor, leilao):
        if valor <= self._saldo:
            if leilao.avaliador(valor, nome=self._nome):
                self.adiciona_saldo(-1*valor)
            else:
                raise ValueError("Você não pode dar um lance "
                                 "menor que o anterior")
        else:
            raise ValueError("Saldo Insuficiente!!")


class Leilao:
    def __init__(self, nome, lance_inicial):
        self._nome = nome
        self._descricao = 'empty'
        self._valor_atual = lance_inicial
        self.lista_lances = [(lance_inicial, 'lance inicial')]

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, mensagem):
        self._descricao = mensagem

    @property
    def valor_atual(self):
        return self._valor_atual

    @valor_atual.setter
    def valor_atual(self, novo_valor):
        self._valor_atual = novo_valor

    def avaliador(self, valor, nome):
        if valor > self.valor_atual:
            self.valor_atual = valor
            self.lista_lances.append((valor, nome))
            return True
        else:
            return False
