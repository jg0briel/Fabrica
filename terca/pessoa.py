#1)
class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        return (f'oi, meu nome é {self.nome}, tenho {self.nome} de idade e trabalho como {self.profissao}.')
    
joao = Pessoa('João', 18, 'programador')    
print(joao.saudacao())

guilherme = Pessoa('Guilherme', 25, 'impresario')
print(guilherme.saudacao())

gabriel = Pessoa('Gabriel', 70, 'aposentado')
print(gabriel.saudacao())
