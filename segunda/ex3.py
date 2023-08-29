#1)
# for l in range(0,11):
#     print(l)

#2)
# for l in range(10,-1,-1):
#     print(l)

#3)
# for l in range(0,11,2):
#     print(l)

#4)
# n = int(input("Digite um número:"))

# print(f"Tabuada de adição do {n}:")
# for l in range(11):
#     ta=n+l
#     print(f"{ta}")

#5)
# nomes = []

# n = input("Digite um nome:")
# while n != "parar":
#     nomes.append(n)
#     n = input("Digite um nome:")
# print(f"Nomes digitados:{nomes}")

#6)
# ns = 0
# n = int(input("Digite um número:"))
# while n != 0:
#     ns = ns + n
#     n = int(input("Digite um número:"))
# print(f"A soma de todos os números é:{ns}")

#7)
f = 0
m = 0
sexo = input("Digite seu sexo (F/M) ou (sair) para encerrar:")
while sexo != "sair":
    if sexo == 'F':
        f = f + 1
    elif sexo == 'M':
        m = m + 1
    sexo = input("Digite seu sexo (F/M) ou (sair) para encerrar:")
print(f"A quantidade de mulheres é:{f}")
print(f"A quantidade de homens é:{m}")