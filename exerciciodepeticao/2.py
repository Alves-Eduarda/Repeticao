mulher = "F"
homem = "M"
s = str(input("sexo [F/M] : "))
while s != mulher and s != homem :
    print("Desculpe, você digitou errado. Tente outra vez!")
    s = str(input("sexo [F/M] : "))
print("Você passou!")