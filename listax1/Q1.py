def elemento_proximo(lista):
    for i in range(len(lista)):
        if i+1 == len(lista):
            continue
        if lista[i] == lista[i+1]:
            return True
        if i+2 == len(lista):
            continue
        if lista[i] == lista[i+2]:
            return True
    return False


def main():
    #lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    lista = [19, 75, 39, 45, 9, 45, 35, 7, 45]
    elemento = 39
    print(elemento_proximo(lista))

if __name__ == '__main__':
    main()