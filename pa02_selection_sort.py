def find_smallest(arr):
    """返回数组中最小值的索引。"""
    smallest = arr[0]
    smallest_i = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_i = i

    return smallest_i


def selection_sort(arr):
    """对数组进行排序。"""
    result = []

    for i in range(len(arr)):
        smallest_i = find_smallest(arr)
        result.append(arr.pop(smallest_i))

    return result


if __name__ == '__main__':
    arr = [1, 4, 2, 7, 5, 8, 6, 3]
    result = selection_sort(arr)
    print(result)

"""
[1, 2, 3, 4, 5, 6, 7, 8]
"""
