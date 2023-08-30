#1)
# class Pessoa():
#     def __init__(self, nome, idade, profissao):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao

#     def saudacao(self):
#         return (f'oi, meu nome é {self.nome}, tenho {self.nome} de idade e trabalho como {self.profissao}.')
    
# joao = Pessoa('João', 18, 'programador')    
# print(joao.saudacao())

#2)
# class ContaBancaria():
#     def __init__(self, titular, saldo, metodos_depositar, metodos_saque):
#         self.titular = titular
#         self.saldo = saldo
#         self.metodos_depositar = metodos_depositar
#         self.metodos_saque = metodos_saque
    
#     def atributos(self):
#         return(f'O titular da conta em questão é {self.titular}, possui um saldo de {self.saldo}, pode depositar pelo {self.metodos_depositar} e pode sacar pelo {self.metodos_saque}.')

# joao = ContaBancaria('João', 2500, 'PIX', 'caixa eletrônico')
# print(joao.atributos())

#3)
# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
    
#     def info(self):
#         return(f'O carro é da marca {self.marca}, modelo {self.modelo} e é do ano {self.ano}.')
    
# carro = Carro('Chevrolet','Opel Corsa', '2024')
# print(carro.info())

#4)
# import math

# class FormaGeomatrica:
#     def calcular_area(self):
#         pass

# class Retangulo(FormaGeomatrica):
#     def __init__ (self, base, altura):
#         self.base = base
#         self.altura = altura

#     def calcular_area(self):
#         return self.base * self.altura

# class Circulo(FormaGeomatrica):
#     def __init__(self, raio):
#         self.raio = raio

#     def calcular_area(self):
#         return math.pi * self.raio ** 2

# retangulo = Retangulo(5, 6)
# print(f"Área do retângulo é: {retangulo.calcular_area()}")

# circulo = Circulo(5)
# print(f"Área do circulo é: {circulo.calcular_area()}")

#5)
class Animal:
    def som(self):
        pass   
    def info_gerais(self):
        pass

class Cachorro(Animal):
    def __init__(self, som_cachorro, info_gerais_cachorro):
        self.som_cachorro = som_cachorro
        self.info_gerais_cachorro = info_gerais_cachorro

    def som(self):
        return self.som_cachorro