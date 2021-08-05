def ser_primo(numb):
    lista = []
    for i in range(1,numb + 1):
        if numb % i == 0:
            lista.append(i)
    if len(lista) <= 2:
        return True
        #print("Esse número é primo")
    else:
        return False
        #print("Esse número não é primo")

if __name__ == '__main__':
    ser_primo(int(input("Que numero quer saber? ")))
