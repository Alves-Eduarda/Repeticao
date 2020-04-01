"""
nome = input("Digite um nome : ")
print(f"Prazer em te conhecer{nome:^20}")
"""
c = "ATENÇÃO"
b = "BOM JOGO"
print(f"{c:~^50}")
print("Você deverá escolher dois números a seguir que atendam aos seguintes critérios : ")
print(f" 1 - O primeiro número deverá ser menor que o segundo; \n 2 - Escolha números inteiros e positivos.\n{b:~^50}")
n1 = int(input("Informe um número : "))
n2 = int(input("Informe um número : "))
s = 0
for c in range (n1,n2,1):
    if c % 2 == 0:
        s += c
if n1 % 2 == 0:
    s1 = s + n1
    print(f"O somatório dos números é : {s1}")
elif n2 % 2 == 0:
    s2 = s + n2
    print(f"O somatório dos números é : {s2}")
elif n1 % 2 == 0 and n2 % 2 == 0 :
    s3 = s + n1 + n2
    print(f"O somatório dos números é : {s3}")


