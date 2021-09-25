class Pessoa:
    olhos = 2 #atributo de classe ou default usado para quando todos os objetos terão o mesmo atributo (permite excessões)
    def __init__(self, *filhos, nome=None, idade=75):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    jefferson = Pessoa (nome='Jefferson' )
    janezy = Pessoa(jefferson, nome='Janezy')

    print(Pessoa.cumprimentar(janezy))
    print(id(janezy))
    print ( id ( jefferson ) )
    print(janezy.cumprimentar())
    print(janezy.nome)
    print(janezy.idade)
    for filho in janezy.filhos:
        print(filho.nome)
    janezy.sobrenome = 'Castro'
    print(janezy.sobrenome)
    del jefferson.filhos
    jefferson.olhos = 3
    print(janezy.__dict__)
    print ( jefferson.__dict__ )
    print(Pessoa.olhos)
    print(jefferson.olhos)
    print(id(Pessoa.olhos), id(janezy.olhos), id(jefferson.olhos))

    print(Pessoa.metodo_estatico(), jefferson.metodo_estatico())
    print ( Pessoa.nome_e_atributo_de_classes (), jefferson.nome_e_atributo_de_classes() )

    print ( Homem.cumprimentar ( janezy ) )