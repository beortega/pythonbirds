class Pessoa:
    def __init__(self, *filhos, nome=None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    beatriz = Pessoa(nome='Beatriz')
    renzo = Pessoa(beatriz, nome='Renzo')
    print(Pessoa.cumprimentar(renzo))
    print(id(renzo))
    print(renzo.cumprimentar())
    print(renzo.nome)
    print(renzo.idade)
    for filho in renzo.filhos:
        print(filho.nome)
    renzo.sobrenome = 'Ramalho'
    del renzo.filhos
    print(renzo.__dict__)
    print(beatriz.__dict__)
