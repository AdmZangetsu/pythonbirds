'''
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1

>>> motor.acelerar()
>>> motor.velocidade
2

>>> motor.acelerar()
>>> motor.velocidade
3


>>> motor.frear()
>>> motor.velocidade
1

>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_esquerda()
>>> carro.calcular_direcao()
'Norte'
'''

class Motor:
    def __init__(self):
        self.velocidade = 0
        self.direcao = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade=max(0, self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
OESTE = 'Oeste'
LESTE = 'Leste'

class Direcao:
    def __init__(self):
        self.valor = NORTE

    def girar_direita(self):
        if self.valor == NORTE:
            self.valor = LESTE

    def girar_esquerda(self):
        if self.valor == LESTE:
            self.valor = NORTE

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_direita(self):
        self.direcao.girar_direita()

    def girar_esquerda(self):
        self.direcao.girar_esquerda()