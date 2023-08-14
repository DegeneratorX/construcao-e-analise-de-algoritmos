def ordenar_duas_listas_como_uma(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] > l2[j]:
                aux = l1[i]
                l1[i] = l2[j]
                l2[j] = aux
    
    insertion_sort(l1)
    insertion_sort(l2)

    print(l1, l2)

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]

        j = i-1
        while j >= 0 and key < lista[j] :
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = key


def main():
    l1 = [5, 9, 1, 7, 3]
    l2 = [4, 2, 10, 6, 8] 
    ordenar_duas_listas_como_uma(l1, l2)

if __name__ == '__main__':
    main()