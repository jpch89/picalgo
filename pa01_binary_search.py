# Python 3
def binary_search(array, item):
    """返回 item 在 array 中的下标，没找到返回 None。"""
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    item = 7
    print(binary_search(array, item))

"""
6
"""
