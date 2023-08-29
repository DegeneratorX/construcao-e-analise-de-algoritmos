"""
Bubble Sort: varre a lista da esquerda para a direita comparando pares de 
elementos consecutivos, e trocando os elementos sempre que o da esquerda é 
maior que o da direita.
"""

def bubble_sort_fisch(lista):
    for i in range(1, len(lista)):
        varredura_fisch(lista, 0, len(lista)-i)


def varredura_fisch(lista, inicio, fim):
    for i in range(inicio, fim):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux


def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    bubble_sort_fisch(lista_desordenada)
    print(lista_desordenada)


if __name__ == '__main__':
    main()
    