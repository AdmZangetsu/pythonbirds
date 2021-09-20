class Pessoa:
    def __init__(self, nome=None, idade=0):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Julio')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print ( p.nome )
    p.nome = 'Jefferson'
    p.idade = '39'
    print(p.nome)
    print(p.idade)