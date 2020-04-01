h = float(input("Informe sua altura : "))
s = input("Informe seu sexo F - feminino / M - masculino : ")
if s == "M":
    p = (72.7*h) - 58
    print(f"Seu peso ideal é {p}")
elif s == "F":
    p = (62.1 *h) - 44.7
    print(f"Seu peso ideal é {p:.2f} ")
