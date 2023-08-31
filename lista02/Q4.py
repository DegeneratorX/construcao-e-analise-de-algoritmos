import numpy as np


def bubble_sort_borboleta(lista):
    for i in range(1, int(np.floor(len(lista)/2))):
        varredura_fisch(lista, 0, int(np.floor(len(lista)/2))-i)
    for i in range(1, int(np.floor(len(lista)/2))):
        varredura_fisch(lista, int(np.floor(len(lista)/2)), len(lista)-i)
    for i in range(1, len(lista)):
        varredura_borboleta(lista, 0, len(lista)-i)
    for i in range(1, int(np.floor(len(lista)/2))):
        varredura_fisch(lista, 0, int(np.floor(len(lista)/2))-i)
    for i in range(1, int(np.floor(len(lista)/2))):
        varredura_fisch(lista, int(np.floor(len(lista)/2)), len(lista)-i)


def varredura_fisch(lista, inicio, fim):
    for i in range(inicio, fim):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux


def varredura_borboleta(lista, inicio, fim):
    for i in range(inicio, fim):
        if len(lista)%2 != 0:
            if fim-i > int(np.floor(len(lista)/2)):
                if lista[i] > lista[fim-i]:
                    aux = lista[i]
                    lista[i] = lista[fim-i]
                    lista[fim-i] = aux
        else:
            if fim-i >= int(np.floor(len(lista)/2)):
                if lista[i] > lista[fim-i]:
                    aux = lista[i]
                    lista[i] = lista[fim-i]
                    lista[fim-i] = aux


def main():
    lista_desordenada = [99999 , 19, 75, 39, 12, 74, 1, 27, 45, 15]
    bubble_sort_borboleta(lista_desordenada)
    print(lista_desordenada)

if __name__ == '__main__':
    main()
