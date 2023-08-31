def particao3(lista, low_pivot, high_pivot):
    # low_index é a posição do último elemento < low_pivot encontrado
    # mid_index é a posição atual sendo considerada
    # high_index é a posição do primeiro elemento > high_pivot encontrado do fim para o início

    low_index = -1
    mid_index = 0
    high_index = len(lista)
    
    while mid_index < high_index:
        # Se o elemento atual é menor que o low_pivot
        if lista[mid_index] < low_pivot:
            low_index += 1
            lista[low_index], lista[mid_index] = lista[mid_index], lista[low_index]
            mid_index += 1
        # Se o elemento atual está entre low_pivot e high_pivot
        elif lista[mid_index] <= high_pivot:
            mid_index += 1
        # Se o elemento atual é maior que high_pivot
        else:
            high_index -= 1
            lista[high_index], lista[mid_index] = lista[mid_index], lista[high_index]
            
    return lista


def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    particao3(lista_desordenada, 30, 70)
    print(lista_desordenada)

if __name__ == '__main__':
    main()