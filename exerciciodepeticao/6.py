soma = count = somapar = par =  0
n = 2000001
for c in range(1,n):
    primo = c % 2
    if primo == 1:
        soma += c
    count +=1
print(f"A soma dos números primos abaixo de {n} é {soma}.")
print(f"O programa rodou {count} vezes.")
print("FIM")