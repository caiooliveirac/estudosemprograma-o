ordem = 'primeiro','segundo','terceiro','quarto'
a = ""
for c in range(len(ordem)):
    a += input(f"Digite o {ordem[c]} número: ")


typl = tuple(a)


print(f"O valor 9 apareceu {typl.count('9')} vezes.")
if "3" in a:
    print(f"O valor 3 foi digitado na posição {typl.index('3')+1}.")
else:
    print("Não escolheram o número 3 em momento algum.")
pares = 0
for i in typl:
    if int(i) % 2 == 0:
        pares += 1
print(f"Apareceram {pares} números pares.")