import random as rd
numbers = ""
for i in range(5):
    sorteio = rd.randint(0,9)
    numbers += f"{sorteio}"
typl = tuple(numbers)

srt = sorted(typl)
print("Sorteamos: ",end="")
for c in range(5):
    print(typl[c],end=" ")


print(f"\nO maior valor entre os sorteados foi {srt[4]}")
print(f"O menor valor entre os sorteados foi {srt[0]}")


