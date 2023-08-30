#1)
# afazeres = []

# while True:
#     print("1. Adicionar tarefa")
#     print("2. Processar tarefa")
#     print("3. Sair")
#     escolha = int(input("Digite sua escolha: "))

#     if escolha == 1:
#         tarefa = input("Digite a tarefa: ")
#         afazeres.append(tarefa)
#     elif escolha == 2:
#         if afazeres:
#             tarefa_atual = afazeres.pop(0)
#             print(f"Tarefa a ser executada no momento: {tarefa_atual}")
#         else:
#             print("A fila de tarefas está vazia")
#     elif escolha == 3:
#         break

#2)
afazeres = []

while True:
    print("1. Adicionar tarefa")
    print("2. Processar tarefa")
    print("3. Sair")
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        tarefa = input("Digite a tarefa: ")
        afazeres.append(tarefa)
    elif escolha == 2:
        if afazeres:
            tarefa_atual = afazeres.pop()
            print(f"Tarefa a ser executada no momento: {tarefa_atual}")
        else:
            print("A fila de tarefas está vazia")
    elif escolha == 3:
        break