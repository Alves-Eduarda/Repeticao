import time
op = maior = menor = soma = multi = 0
n = int(input(" Primeiro número : "))
n1 = int(input(" Segundo número : "))
while op != 5 :
    print(" [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa")
    op = int(input("Escolha a opçäo desejada: "))
    if op > 5:
        print("Opção inválida! Tente novamente.")
    if op == 1:
        soma = n + n1
        print(f"A soma dos números digitados vale : {soma}")
    if op == 2:
        multi = n*n1
        print(f"A multiplicação dos número digitados vale : {multi}")
    if op == 3:
        if n > n1 :
            maior = n
            print(f"O maior número digitado foi : {maior}")
        elif n == n1:
            print("Os valores digitados são iguais.")
        else:
            print(f"O maior número digitado foi : {maior}")
    if op == 4:
        n= int(input("Digite um número : "))
        n1= int(input("Digite um número : "))
print("Finalizando....")
seg = time.sleep(1)
print("#"*30)
print("Você saiu do jogo! Volte sempre")
