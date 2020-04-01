import time
while True:
    n = int(input("Quer ver a tabuada de qual número ? "))
    if n < 0:
        print("Programa encerrado.")
        break
    print("~"*20, "TABUADA", "~"*20)
    print(f"A tabuada do número {n} é:  ")
    for c in range (1,11):
        m = c * n
        t = time.sleep(1)
        print(f"{c} * {n} : {m} ")
