

typl = []
while len(typl) < 6:
    objet = input("Diga o nome do item: ")
    typl.append(objet)
    preco = input("O preço dele: ")
    typl.append(preco)

tupl = tuple(typl)
print('-'*35)
print('LISTAGEM DE PREÇOS'.center(35))
print('-'*35)
for i in range(0,len(tupl),2):
    print(f"{tupl[i]}",'-'*(33-len(tupl[i])-len(tupl[i+1])),f"{tupl[i+1]}")

print('-'*35)

