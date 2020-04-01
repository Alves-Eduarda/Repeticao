maior = 0
menor = 0
for c in range (1,6):
    p = float(input(f"O peso da {c} pessoa: "))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f"O maior peso lido foi {maior}Kg")
print(f"O menor peso lido foi {menor}Kg")