def ordenacao_unimodal(lista, k):
    # Ordenação crescente até k
    for i in range(k):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    # Ordenação decrescente depois de k
    for i in range(k, len(lista) - 1):
        for j in range(i, len(lista) - 1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    print(lista)


def main():
    lista = [5, 3, 2, 4, 1, 6, 0]
    ordenacao_unimodal(lista, 4)


if __name__ == '__main__':
    main()