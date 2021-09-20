class Pessoa:
    def __init__(self, *filhos, nome=None, idade=75):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    jefferson = Pessoa (nome='Jefferson' )
    janezy = Pessoa(jefferson, nome='Janezy')

    print(Pessoa.cumprimentar(janezy))
    print(id(janezy))
    print(janezy.cumprimentar())
    print(janezy.nome)
    print(janezy.idade)
    for filho in janezy.filhos:
        print(filho.nome)

