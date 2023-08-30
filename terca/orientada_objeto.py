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
# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo

#     def mostrar_saldo(self):
#         print(f'seu saldo: {self.saldo}')
#     def depositar(self, dinheiro):
#         self.saldo += dinheiro

#     def sacar_dinheiro(self, valor):
#         if valor > self.saldo:
#             print('voce nao pode sacar =)')
#         else:
#             self.saldo -= valor

    
# joao = ContaBancaria('joao', 0)
# joao.depositar(50)
# joao.mostrar_saldo()

# joao.sacar_dinheiro(200)
# joao.mostrar_saldo()

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
# class FormalaGeometrica:
#     def calcular_area(self, raio):
#         return 3.14*(raio**2)
    
# class Circulo(FormalaGeometrica):
#     pass

# class Retangulo(FormalaGeometrica):
#     def calcular_area(self, base, altura):
#         return base*altura
    
# circulo = Circulo()
# area = circulo.calcular_area(20)
# print(area)

# retangulo = Retangulo()
# area = retangulo.calcular_area(5,10)
# print(area)

#5)
class Animal:
    def animal(self, som, info):
        return(f"O cachorro faz {som} e tem como características {info}")

class Cachorro(Animal):
    pass

class Gato(Animal):
    def animal(self, som_gato, info_gato):
        return (f'O gato faz {som_gato} e suas caracteristicas gerais são {info_gato}.')

cachorro = Cachorro()
dog = cachorro.animal("auau", "quatro patas, um rabo, bom olfato")
print(dog)

gato = Gato()
cat = gato.animal("miau", "quatro patas, um rabo, boa visão")
print(cat)