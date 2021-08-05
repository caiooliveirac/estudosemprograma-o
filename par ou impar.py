import random

print("PAR OU ÍMPAR?")

temporiz = 1

while temporiz > 0:
    pimp = input("Quer par ou ímpar? ")
    numer = int(input("Diga o seu número: "))
    adver = random.randint(0,5)

    print(f"O computador escolheu {adver}")

    ad = ""

    if (numer + adver) % 2 == 0:
        if pimp.lower() == "impar":
            ad = "perdeu"
        elif pimp.lower() == "ímpar":
            ad = "perdeu"
            break
        else:
            ad = "ganhou"
            temporiz += 1
            print(f"Você {ad}")
    else:
        if pimp.lower() == "par":
            ad = "perdeu"
            break
        else:
            ad = "ganhou"
            temporiz += 1
            print(f"Você {ad}")

print(f"Você {ad}")