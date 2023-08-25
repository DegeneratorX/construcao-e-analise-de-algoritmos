# Atenção: bubble sort modificado
def ordenacao_par_impar(lista):
    n = len(lista)
    # Ordenando elementos em posições ímpares
    for i in range(1, n, 2):  # Começando em 1 para índices ímpares
        for j in range(1, n-i, 2):
            if lista[j] > lista[j+2]:
                lista[j], lista[j+2] = lista[j+2], lista[j]

    # Ordenando elementos em posições pares
    for i in range(0, n, 2):  # Começando em 0 para índices pares
        for j in range(0, n-i-2, 2):
            if lista[j] > lista[j+2]:
                lista[j], lista[j+2] = lista[j+2], lista[j]

    print(lista)


def main():
    lista = [5, 3, 2, 4, 7, 1, 6, 0]
    ordenacao_par_impar(lista)


if __name__ == '__main__':
    main()
