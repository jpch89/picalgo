"""
此处采用算法动画图解 APP 的方式，
构建开销表的时候除了起点，
其余节点开销都设置为正无穷，
起点的开销为 0。
"""
import time

# 构建图
graph = {}
# start
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['c'] = 2
# a
graph['a'] = {}
graph['a']['b'] = 4
graph['a']['d'] = 2
# b
graph['b'] = {}
graph['b']['end'] = 3
graph['b']['d'] = 6
# c
graph['c'] = {}
graph['c']['a'] = 8
graph['c']['d'] = 7
# d
graph['d'] = {}
graph['d']['end'] = 1
# end
graph['end'] = {}

# 构建开销表
inf = float('inf')
costs = {}.fromkeys(['start', 'a', 'b', 'c', 'd', 'end'], inf)
costs['start'] = 0

# 构建父节点表
parents = {}.fromkeys(['a', 'b', 'c', 'd', 'end'])


def get_lowest(costs, processed):
    """返回开销表中开销最低的节点和最低开销。"""
    lowest_node = None
    lowest_cost = inf
    for node, cost in costs.items():
        if node in processed:
            continue
        if cost < lowest_cost:
            lowest_cost = cost
            lowest_node = node
    return lowest_node, lowest_cost


def dijkstra():
    """使用狄克斯特拉算法，返回路径和最低开销。"""
    # 记录已处理节点
    processed = []

    while True:
        # 找到开销表中开销最低的节点和最低开销
        l_node, l_cost = get_lowest(costs, processed)
        if l_node is None:
            break
        # 遍历该节点的邻居，计算并更新开销
        neighbors = graph[l_node]
        for neighbor, neighbor_cost in neighbors.items():
            new_cost = l_cost + neighbor_cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = l_node
        # 追加已处理节点
        processed.append(l_node)

    # 最低开销路径
    path_li = ['end']
    while path_li[0] != 'start':
        for child, parent in parents.items():
            if child == path_li[0]:
                path_li.insert(0, parent)
    path = ' >>> '.join(path_li)
    path_cost = costs['end']
    return path, path_cost


if __name__ == '__main__':
    path, path_cost = dijkstra()
    print('最低开销路径为: %s' % path)
    print('最低开销为：%d' % path_cost)
"""
最低开销路径为: start >>> a >>> d >>> end
最低开销为：8
"""
