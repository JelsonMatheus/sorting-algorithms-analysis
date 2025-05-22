import time
import random

from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quicksort import quicksort
from algorithms.heap_sort import heap_sort


def measure_time(func, arr):
    repetitions = 3
    total_time = 0
    for _ in range(repetitions):
        copy_arr = arr.copy()
        start_time = time.time()
        func(copy_arr)
        total_time += time.time() - start_time
    return total_time / repetitions


def measure_time_bubble(arr):
    return measure_time(bubble_sort, arr)


def measure_time_insertion(arr):
    return measure_time(insertion_sort, arr)


def measure_time_merge(arr):
    return measure_time(lambda a: merge_sort(a, 0, len(a) - 1), arr)


def measure_time_heap(arr):
    return measure_time(heap_sort, arr)


def measure_time_quick(arr):
    return measure_time(lambda a: quicksort(a, 0, len(a) - 1), arr)


def main():
    size = 501

    vector = list(range(size))
    ascending = sorted(vector)  # Crescente
    descending = sorted(vector, reverse=True)  # Decrescente
    random_arr = vector.copy()  # Aleatório
    random.shuffle(random_arr)

    # Testando Bubble Sort
    bubble_ascending_time = measure_time_bubble(ascending.copy())
    print(f"\nBubbleSort Crescente -  {bubble_ascending_time:.5f} segundos")

    bubble_descending_time = measure_time_bubble(descending.copy())
    print(f"BubbleSort Decrescente - {bubble_descending_time:.5f} segundos")

    bubble_random_time = measure_time_bubble(random_arr.copy())
    print(f"BubbleSort Aleatorio - : {bubble_random_time:.5f} segundos")
    print('\n')

    # Testando Insertion Sort
    insertion_ascending_time = measure_time_insertion(ascending.copy())
    print(f"InsertionSort Crescente - {insertion_ascending_time:.5f} segundos")

    insertion_descending_time = measure_time_insertion(descending.copy())
    print(f"InsertionSort Decrescente - {insertion_descending_time:.5f} segundos")

    insertion_random_time = measure_time_insertion(random_arr.copy())
    print(f"InsertionSort Aleatório {insertion_random_time:.5f} segundos")
    print('\n')

    # Testando Merge Sort
    merge_ascending_time = measure_time_merge(ascending.copy())
    print(f"MergeSort Crescente - {merge_ascending_time:.5f} segundos")

    merge_descending_time = measure_time_merge(descending.copy())
    print(f"MergeSort Decrescente - {merge_descending_time:.5f} segundos")

    merge_random_time = measure_time_merge(random_arr.copy())
    print(f"MergeSort Aleatório -  {merge_random_time:.5f} segundos")
    print('\n')

    # Testando Heap Sort
    heap_ascending_time = measure_time_heap(ascending.copy())
    print(f"HeapSort Crescente: {heap_ascending_time:.5f} segundos")

    heap_descending_time = measure_time_heap(descending.copy())
    print(f"HeapSort Decrescente - {heap_descending_time:.5f} segundos")

    heap_random_time = measure_time_heap(random_arr.copy())
    print(f"HeapSort Aleatório - {heap_random_time:.5f} segundos")
    print('\n')

    # Testando Quick Sort
    quick_ascending_time = measure_time_quick(ascending.copy())
    print(f"QuickSort Crescente - {quick_ascending_time:.5f} segundos")

    quick_descending_time = measure_time_quick(descending.copy())
    print(f"QuickSort Decrescente - {quick_descending_time:.5f} segundos")

    quick_random_time = measure_time_quick(random_arr.copy())
    print(f"QuickSort Aleatorio - {quick_random_time:.5f} segundos")



if __name__ == "__main__":
    main()