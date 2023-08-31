def particao(lista, esq, dir):
    pivo = lista[dir]
    i = esq - 1
    for j in range(esq, dir):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[dir] = lista[dir], lista[i+1]
    return i+1

def quickSelect(lista, esq, dir, k):
    if esq == dir:
        return lista[esq]
    
    # Partição é o mesmo do Quicksort
    indice_pivo = particao(lista, esq, dir)
    
    # Se o pivô for o k-ésimo, retorna ele
    if k == indice_pivo:
        return lista[k]
    # Se k for menor, procurar na metade esquerda
    elif k < indice_pivo:
        return quickSelect(lista, esq, indice_pivo-1, k)
    # Se k for maior, procurar na metade direita
    else:
        return quickSelect(lista, indice_pivo+1, dir, k)

# Função para encontrar o k-ésimo menor elemento
def menor(lista, k):
    # Ajuste já que a indexação em Python começa em 0
    return quickSelect(lista, 0, len(lista)-1, k-1)

def main():
    lista_desordenada = [19, 75, 39, 12, 74, 1, 27, 45, 15]
    a = menor(lista_desordenada, 3)
    print(lista_desordenada, a)

if __name__ == '__main__':
    main()