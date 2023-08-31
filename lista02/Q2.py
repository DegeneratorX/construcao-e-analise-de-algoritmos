import numpy as np


def bubble_sort_tercos(lista):
    um_tercos = int(np.floor(len(lista)/3))
    dois_tercos = int(np.floor(2*len(lista)/3))
    for i in range(1, dois_tercos):
        varredura_fisch(lista, 0, dois_tercos-i)
    for i in range(1, dois_tercos):
        varredura_fisch(lista, um_tercos, len(lista)-i)
    for i in range(1, dois_tercos):
        varredura_fisch(lista, 0, dois_tercos-i)


def varredura_fisch(lista, inicio, fim):
    for i in range(inicio, fim):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux


def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    bubble_sort_tercos(lista_desordenada)
    print(lista_desordenada)

if __name__ == '__main__':
    main()
