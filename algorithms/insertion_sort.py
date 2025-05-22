# Implementação de Insertion Sort conforme o Cormen

def insertion_sort(arr):
    for j in range(1, len(arr)):
        chave = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > chave:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = chave
