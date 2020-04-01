primo = soma = 0
for c in range (1,31):
    primo = c % 2
    if primo == 1:
        soma += c
        print(c, end= " ")
print(soma)
