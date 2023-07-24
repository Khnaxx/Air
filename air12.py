import sys

def partition(arr, first, last):
    pivot = arr[last]
    i = first - 1
    for j in range(first, last):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return i + 1


def quick_sort(arr, first, last):
    if first < last:
        pivot = partition(arr, first, last)
        quick_sort(arr, first, pivot-1)
        quick_sort(arr, pivot+1, last)
    return arr

if __name__ == "__main__":
    table = sys.argv[1:]
    N = len(table)
    quick_sort(table, 0, N-1)
    print(table)
