#1)
# n1 = int(input("Digite sua idade:"))

# if n1 >= 18:
#     print("Pode obter o CNH")
# else:
#     print("Não pode obter CNH")

#2)
# n1 = int(input("Digite a velocideda que você passou:"))
# valor_multa = 7
# ex = n1 - 80
# multa = valor_multa*ex
# if n1 > 80:
#     (print(f"Você foi multado em:{multa} reais"))
# else:
#     print("Velocidade normal")

#3)
# n1= float(input("Digite um número:"))
# n2= float(input("Digite outro número:"))
# n3= float(input("Digite outro número:"))
# maior = n1
# menor = n1

# if n2 > maior:
#     maior = n2
# if n3 > maior:
#     maior = n3

# if n2 < menor:
#     menor = n2
# if n3 < menor:
#     menor = n3

# print(f"O maior é:{maior}")
# print(f"O menor é:{menor}")

#4)
# n1 = int(input("Digite quantas canetas azuis você comprou:"))
# n2 = int(input("Digite quantas canetas pretas você comprou:"))
# pz=n1*2
# pt=n2*2.5

# print("A quantidade total a ser paga é:",pz+pt)

#5)
nome = input("Digite seu nome:")

if nome == "João Maia":
    print("Oi eu sou João Maia'")
elif nome == "João Abrantes":
    print("Oi eu sou joao abrantes")
elif nome == "Pedro":
    print("Oi eu sou pedro")
else:
    print(f"Oi, meu nome é {nome}")