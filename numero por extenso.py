cont = ('um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    ask = int(input("Diga um número de um a dezesseis: "))

    if 0 <= ask <= 20:
        print (f"Você digitou {cont[ask-1]}")
    else:
        print("Tente novamente. ", end="")
    dnv = "A"
    while 0 <= ask <= 20:
        dnv = input("Quer de novo [s/n]? ")
        if dnv in "Nn":
            print("Ok.Encerrado.")

        elif dnv in "Ss":
            break
    if dnv in "Nn":
        break








