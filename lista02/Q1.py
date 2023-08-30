def bubble_sort_particionada(lista, k):
    lista1, lista2 = particiona(lista, k)
    for i in range(1, len(lista1)):
        varredura_fisch(lista1, 0, len(lista1)-i)
    for i in range(1, len(lista2)):
        varredura_fisch(lista2, 0, len(lista2)-i)

    lista_final = lista1
    lista_final.append(lista[k])
    lista_final = lista_final + lista2
    return lista_final
    

def varredura_fisch(lista, inicio, fim):
    for i in range(inicio, fim):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux


def particiona(lista, k):
    lista1, lista2 = [], []
    for i in range(k):
        lista1.append(lista[i])
    for i in range(k+1, len(lista)):
        lista2.append(lista[i])
    return lista1, lista2



def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    lista_final = bubble_sort_particionada(lista_desordenada, 4)
    print(lista_final)


if __name__ == '__main__':
    main()
