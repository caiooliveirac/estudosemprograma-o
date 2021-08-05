tupla = ('jogo','python','node','infinity','school','dev')
lista = []

vow = 0
for i in tupla:
    a = list(i)
    for c in a:
        if c.lower() in "aeiou":
            vow += 1

print(vow)

for p in range(0,len(tupla)):
    print(f"Na palavra {tupla[p]} temos as vogais", end=" ")
    vow=0
    a = list(tupla[p])
    for c in a:
        if c.lower() in "aeiou":
            vow += 1
            print(c,end=", ")


    print(f"sendo {vow} vogais.")