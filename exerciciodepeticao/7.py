import time
somaconsumo = cmenor1 =cmenor2 = cmenor3 = cmaior1 = cmaior2 = cmaior3 = count1 = count2 = count3 = media = 0
n = int(input("Informe o número de habitantes da cidade : "))
kwh = float(input("Informe o valor do Kwh da cidade : "))
for c in range (1, n+1):
    print("~"*5,"Insira os dado abaixo, conforme solicitado","~"*5)
    c = float(input("Informe o consumo de energia por mês : "))
    print(" 1 - Residencial \n 2 - Comercial \n 3 - Industrial ")
    t = int(input("De acordo com seu tipo de consumo,escolha uma das opções dadas acima: "))
    while t != 1 and t != 2 and t!= 3 :
        print("Opção inválida! Digite novamente.")
        t = int(input("De acordo com seu tipo de consumo,escolha uma das opções dadas acima: "))
    somaconsumo +=c
    if t == 1:
        count1 +=c
        cmaior1 = c
        cmenor1 = c
        if c > cmaior1:
            cmaior1 = c
        else:
            cmenor1 = c
    if t == 2:
        count2 += c
        cmaior2 = c
        cmenor2 = c
        if c > cmaior2:
            cmaior = c
        else:
            cmenor = c
    if t == 3:
        count3 += c
        cmaior3 = c
        cmenor3 = c
        if c > cmaior3:
            cmaior3 = c
        else:
            cmenor3 =c
media = somaconsumo/kwh
print("FINALIZANDO...")
seg = time.sleep(2)
print("~"*15)
print(f"A média do consumo da cidade é {media}")
print(f"O total de consumo do grupo 1 é {count1} \nO total de consumo do grupo 2 é {count2} \nO total de consumo do grupo 3 é {count3}")
print(f"O maior consumidor do grupo 1 é {cmaior1} \nO maior consumidor do grupo 2 é {cmaior2} \nO maior consumidor do grupo 3 é {cmaior3}")
print(f"O menor consumidor do grupo 1 é {cmenor1} \nO menor consumidor do grupo 1 é {cmenor2} \nO menor consumidor do grupo 2 é {cmenor3}")
