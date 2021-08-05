lista = []

while True:
    a = int(input("Que número deseja listar? "))
    if a not in lista:
        lista.append(a)
        cont = input("Quer continuar? [s/n]")
    else:
        print("Esse valor já estava na lista. Não adicionarei de novo.")
    if cont in "Nn":
        break
print(f"Essa é sua lista: {lista}")