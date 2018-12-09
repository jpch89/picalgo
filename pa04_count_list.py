def count_list(li):
    """计算列表中包含的元素个数。"""
    if not li:
        return 0
    else:
        return 1 + count_list(li[1:])


if __name__ == '__main__':
    li = [1, 2, 3]
    print(count_list(li))

"""
3
"""
