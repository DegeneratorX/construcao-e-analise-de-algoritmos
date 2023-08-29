"""
Selection Sort: percorre toda a lista, verifica qual o maior, troca com o menor
na posição atual.

"""


# Selection sort que coloca os maiores elementos no final
def selection_sort_fisch(lista):
    for i in range(1, len(lista)):
        indice_maior = posicao_maior_fisch(lista, 0, len(lista)-i)
        aux = lista[indice_maior]
        lista[indice_maior] = lista[len(lista)-i]
        lista[len(lista)-i] = aux


def posicao_maior_fisch(lista, inicio, fim):
    maior = lista[inicio]
    indice_maior = inicio
    for i in range(inicio+1, fim+1):
        if lista[i] > maior: 
            maior = lista[i]
            indice_maior = i
    return indice_maior



# Selection sort que coloca os menores elementos no começo
def selection_sort_wiki(lista):
    for i in range(len(lista)):
        menor = i

        for j in range(i+1,len(lista)):
            if lista[j] < lista[menor]:
                    menor = j

        if lista[i] != lista[menor]:
                aux = lista[i]
                lista[i] = lista[menor]
                lista[menor] = aux


def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    #selection_sort_fisch(lista_desordenada)
    selection_sort_wiki(lista_desordenada)
    print(lista_desordenada)


if __name__ == '__main__':
    main()
