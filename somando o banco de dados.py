print("SOMANDO O BANCO DE DADOS")
print("="*20)

soma = 0
elem = 0

while True:
    numer = int(input("Me dê o número: "))
    if numer == 999:
        break
    soma += numer
    elem += 1


print(soma,elem)