def somar(a, b):
    print(a+b)

def divide(a, b):
    if (b == 0):
        print ("divisao por 0")
    else:
        print(f'O resultado da divisao entre: {a} e {b} e: {a/b}')
divide(5, 5)

def multiplicar(a, b):
    print(a*b)


print ("Para somar, digite 1")
print ("Para multiplicar, digite 2")
print ("Para divide, digite 3")

selecionador = int (input("digite o numero da operacao: "))
numero1 = int(input("primeiro numero: "))
numero2 = int(input("segundo numero: "))

if (selecionador == 1):
    somar(numero1, numero2)

elif (selecionador == 2):
    multiplicar(numero1, numero2)
elif (selecionador == 3):
    divide(numero1, numero2)