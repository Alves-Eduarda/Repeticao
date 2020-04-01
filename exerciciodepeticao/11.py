import random
n = num = cont = 0
print("~"*20,"Vamos jogar PAR ou ÍMPAR", "~"*20)
n = random.randint(0,10)
comp = " "
while True:
    num = int(input("Infome um número : "))
    t = str(input("Você escolhe [P/I] ? ")).upper().strip()
    while t != "P" and t != "I":
        print("Informe novamente sua escolha")
        t = str(input("Você escolhe [P/I] ? ")).upper().strip()
    if t == "P":
        comp = "I"
        soma = num + n
        par = soma % 2
        if par == 0 and comp == "I":
            cont+=1
            print(f"Você jogou {num} e o Computador jogou {n}. Total de {soma} DEU PAR")
            print("~" * 40)
            print(" Você venceu \n Vamos tentar novamente")
            print("~" * 40)
        elif par == 1 and comp == "I":
            print(f" Você jogou {num} e o Computador jogou {n}. Total de {soma} DEU IMPAR")
            print(f" Você venceu {cont} vezes")
            break
    if t == "I":
        comp = "P"
        soma = num + n
        impar = soma % 2
        if impar == 1 and comp == "P":
            cont += 1
            print(f" Você jogou {num} e o Computador jogou {n}. Total de {soma} DEU IMPAR")
            print("~" * 40)
            print(" Você venceu \n Vamos jogar novamente")
            print("~"*40)
        elif impar == 0 and comp == "P":
            print(f" Você jogou {num} e o Computador jogou {n}. Total de {soma} DEU PAR")
            print(f" Você venceu {cont} vezes")
            break



