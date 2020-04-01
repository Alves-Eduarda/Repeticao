import random
print("~"*20,"TENTE ADIVINHAR O NÚMERO EM QUE ESTOU PENSANDO!","~"*20)
n = random.randint(0,10)
u = int(input("Digite um valor entre 0 e 10 : "))
c = 0
while u != n :
    print("VOCÊ PERDEU! \nVAMOS TENTAR NOVAMENTE!")
    u = int(input("Digite um valor entre 0 e 10 : "))
    c +=1
print(f"Após {c} tentativas...")
print("~"*20,"VOCÊ ME VENCEU!","~"*20)
