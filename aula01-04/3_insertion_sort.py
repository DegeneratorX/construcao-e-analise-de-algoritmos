"""
Insertion Sort: troca o elemento atual com o anterior enquanto ele for menor 
do que o anterior. Ou seja, leva o menor da lista até o início, pulando de
número em número.
"""


def insertion_sort_fisch(lista):
    for i in range(1, len(lista)):
        while i > 0 and lista[i] < lista[i-1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
            i -= 1


def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    insertion_sort_fisch(lista_desordenada)
    print(lista_desordenada)


if __name__ == '__main__':
    main()
    