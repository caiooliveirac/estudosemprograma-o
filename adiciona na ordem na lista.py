lista = []

prim = int(input("Digite o valor para adicionar: "))
lista.append(prim)
print("Adicionado ao fim da lista.")

for i in range(4):
    itens = int(input("Digite o valor para adicionar: "))
    if itens > lista[0]:
        if itens > lista[1]:
            if itens > lista[2]:
        lista.insert(len(lista)-1, itens)
    elif itens < lista[len(lista)-2]:
        lista.insert(len(lista) - 2, itens)
    elif itens < lista[len(lista)-3]:
        lista.insert(len(lista) - 3, itens)
    else:
        lista.insert(len(lista), itens)

print(lista)