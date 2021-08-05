
maiores = 0
homens = 0
mulheres = 0
while True:
    idade = int(input("Qual a idade? "))
    if idade > 18:
        maiores += 1
    sexo = input("Qual o sexo? ")
    if sexo in "masc":
        homens += 1
    if "f" in sexo and idade < 20:
        mulheres += 1
    contin = input("Quer continuar? ")
    if contin in "n":
        break

print(maiores,homens,mulheres)