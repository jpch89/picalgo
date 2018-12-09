def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    first = arr[0]
    second = find_max(arr[1:])
    return first if first > second else second


if __name__ == '__main__':
    arr = [1, 7, 4, 8]
    print(find_max(arr))

"""
8
"""
