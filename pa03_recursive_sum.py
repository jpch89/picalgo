def recursive_sum(arr):
    """使用递归对数组求和。"""
    if not arr:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])


if __name__ == '__main__':
    arr = [1, 2, 3]
    print(recursive_sum(arr))

"""
6
"""
