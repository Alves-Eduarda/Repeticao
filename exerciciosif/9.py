s = 0
velho = 0
mulheridade = 0
for c in range (1,5) :
    nome = str(input(f"Nome da {c} pessoa : ")).strip()
    idade = int(input(f"Idade da {c} pessoa : "))
    sexo = str(input(f"Sexo da {c} pessoa ( F - feminino / M - masculino: ")).upper()
    s += idade
    if c == 1 and sexo == "M":
        velho = idade
        nomevelho = nome
    else:
        if idade > velho:
            velho = idade
            nomevelho = nome
    if sexo == "F" and idade < 20 :
        mulheridade += 1
m = s/4
print(f"A média da idade do grupo é de {m}")
print(f"O homem mais velho é {nomevelho} com {velho} anos.")
print(f"Temos {mulheridade} mulher (es) com idade menor que 20 anos")