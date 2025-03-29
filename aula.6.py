a = [4, 7, 8]

lista = [] #instanciar uma lista vazia
lista.append(1) #adicionar elementos a lista
lista.append(2) #adicionar elementos a lista
lista.append(3) #adicionar elementos a lista

li = []
elemento = lista.pop() #remover elementos da lista 
print(elemento) #saida:3

iterador = 0
while iterador <= 10:
    li.append(iterador)
    print(f"iterador: {iterador} elemento{li[iterador]}")
    iterador += 1


def fibonacci (num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibonacci (num - 1) + fibonacci (num -2)
    
print (fibonacci(7))