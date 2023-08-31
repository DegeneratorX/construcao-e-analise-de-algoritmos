def bubble_sort_parimpar(lista):
    for i in range(1, len(lista)):
        varredura_fisch_parimpar(lista, 0, len(lista)-i)
    for i in range(1, len(lista)):
        varredura_fisch(lista, 0, len(lista)-i)


def varredura_fisch_parimpar(lista, inicio, fim):
    for i in range(inicio, fim-1, 2):
        if lista[i] > lista[i + 2]:
            aux = lista[i]
            lista[i] = lista[i+2]
            lista[i+2] = aux
    for i in range(inicio+1, fim-1, 2):
        if lista[i] > lista[i + 2]:
            aux = lista[i]
            lista[i] = lista[i+2]
            lista[i+2] = aux

def varredura_fisch(lista, inicio, fim):
    for i in range(inicio, fim):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux


def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    bubble_sort_parimpar(lista_desordenada)
    print(lista_desordenada)

if __name__ == '__main__':
    main()
