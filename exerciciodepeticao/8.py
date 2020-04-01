media = maior = menor = count = soma =  0
resposta = "S"
while resposta == "S":
    n = int(input("Informe um número : "))
    resposta = str(input("Deseja continuar ? [S/N] : ")).upper()
    count += 1
    soma += n
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media= soma/count
print(f"Você digitou {count} números e a média dos valores digitados foi {media:.2f} ")
print(f"O menor valor digitado foi {menor} e o maior digitado foi {maior}")
