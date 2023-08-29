#1)
def idade(x):
    return (x)

n1 = int(input("Digite sua idade:"))
r = idade(n1)
if r < 18:
    print("Não possui CNH")
else:
    print("Possui CNH")

#2)
# def multa(x,y,z):
#     return(x-y)*z

# n1 = int(input("Digite a velocideda que você passou:"))
# valor_multa = 7
# ex = 80
# r = multa(n1, ex, valor_multa)

# if r > 80:
#     (print(f"Você foi multado em:{r} reais"))
# else:
#     print("Velocidade normal")

#3)
# def classe():

#     n1= float(input("Digite um número:"))
#     n2= float(input("Digite outro número:"))
#     n3= float(input("Digite outro número:"))
#     maior = n1
#     menor = n1
    
#     if n2 > maior:
#         maior = n2
#     if n3 > maior:
#         maior = n3

#     if n2 < menor:
#         menor = n2
#     if n3 < menor:
#         menor = n3

#     print(f"O maior é:{maior}")
#     print(f"O menor é:{menor}")
#classe()

#4)
# def total(x,y):
#     return (x*2) + (y*2.5)
# n1 = int(input("Digite quantas canetas azuis você comprou:"))
# n2 = int(input("Digite quantas canetas pretas você comprou:"))
# r = total(n1, n2)

# print(f"A quantidade total a ser paga é:{r}")

#5)
# def oi(x):
#     return(x)

# nome = input("Digite seu nome:")
# r=(nome)

# if r == "João Maia":
#     print("Oi eu sou João Maia'")
# elif r == "João Abrantes":
#     print("Oi eu sou joao abrantes")
# elif r == "Pedro":
#     print("Oi eu sou pedro")
# else:
#     print(f"Oi, meu nome é {r}")