def qsort(arr):
    if len(arr) < 2:
        return arr

    pivot, arr = arr[0], arr[1:]
    smaller = []
    bigger = []

    for i in arr:
        if i <= pivot:
            smaller.append(i)
        else:
            bigger.append(i)

    return qsort(smaller) + [pivot] + qsort(bigger)


if __name__ == '__main__':
    arr = [1, 4, 2, 7, 5, 3, 8, 9, 6]
    print(qsort(arr))
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
