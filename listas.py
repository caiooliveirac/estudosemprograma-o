lista = []

for i in range(5):
    item = input(f"Digite o valor número {i+1}: ")
    lista.append(item)
print(lista)
aba = sorted(lista)
print(aba)
print(f"O menor valor é o {aba[0]} e o maior é o {aba[4]}.")
