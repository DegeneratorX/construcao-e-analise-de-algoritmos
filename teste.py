def merge_sorted_lists(L1, L2):
    i = j = 0  # Índices para percorrer as listas L1 e L2, respectivamente
    result = []  # Lista para armazenar a mesclagem ordenada
    
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    
    # Adicionar os elementos restantes, se houver, de L1 e L2
    result.extend(L1[i:])
    result.extend(L2[j:])
    
    return result

# Exemplo de uso
n = 5  # Tamanho das listas L1 e L2
L1 = [1, 3, 5, 7, 9]  # Lista ordenada 1
L2 = [2, 4, 6, 8, 10]  # Lista ordenada 2

merged_list = merge_sorted_lists(L1, L2)
print(merged_list)
