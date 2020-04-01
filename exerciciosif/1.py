from math import sqrt
num = float(input("Informe um número : "))
if num < 0:
    print("Valor inválido")
else:
    raiz = sqrt(num)
    print(raiz)