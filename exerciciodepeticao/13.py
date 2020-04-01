soma = cont = menor = preco = c = 0
menornome = ' '
while True:
    nome = str(input("Informe o nome do produto : ")).strip()
    preco = float(input("Informe o preço do produto : "))
    soma += preco
    c += 1
    t = str(input("Deseja continuar [S/N] ? ")).upper()
    while t not in "SN":
        t = str(input("Deseja continuar [S/N] ? ")).upper()
    if t == "N":
        break
    if preco > 1000:
        cont += 1
    if c == 1 or preco < menor:
        menor = preco
        menornome = nome
print("~"*10,"Programa encerrado. Observe os dados coletados...","~"*10)
print(f" O total gasto na compra foi R$ {soma:.2f} reais \n {cont} produtos custam mais de R$ 1000 reais. \n O produto mais barato é {menornome}")