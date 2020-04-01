cont = ch = cm = 0
while True:
    idade = int(input("Idade : "))
    if idade > 18:
        cont += 1
    sexo = str(input("sexo [F/M] : ")).upper().strip()
    while sexo not in "FM":
        sexo = str(input("sexo [F/M] : ")).upper().strip()
    if sexo =="M":
        ch +=1
    if sexo == "F" and idade < 20:
        cm +=1
    n = str(input("Deseja continuar [S/N]: ")).upper().strip()
    while n not in "SN":
        n = str(input("Deseja continuar [S/N]: ")).upper().strip()
    if n == "N":
        print(" Programa encerrado. Observe os dados coletados... ")
        break
print(f" Foram cadastradas {cont} pessoa(s) maior(es) de 18 anos.\n Foram cadastrados {ch} homens.\n Foram cadastradas {cm} mulheres com menos de 20 anos.")