def calculadora():
    def soma(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        return a / b
    
    var = input('Operação: ')
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))
    
    if var == 'soma':
        resultado = soma(num1, num2)
    elif var == 'sub':
        resultado = sub(num1, num2)
    elif var == 'mult':
        resultado = mult(num1, num2)
    elif var == 'div':
        resultado = div(num1, num2)
    else:
        resultado = "Operação não reconhecida"
    
    print("Resultado:", resultado)

calculadora()
