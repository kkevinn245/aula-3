def fatorial (a):
    if a == 0:
     return 1
    else:
     print(a)
     return a * fatorial(a-1)
numero = 1
entrada = int(input("numero parra calcular o fatorial"))
while numero <= entrada:
    print(f"fatorial de : {numero}: {fatorial(numero)}")
    numero = numero + 1 