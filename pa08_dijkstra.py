# 创建图
graph = {}
# start
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# A
graph['a'] = {}
graph['a']['end'] = 1
# B
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
# end
graph['end'] = {}  # 终点没有任何邻居

# 创建开销的散列表
inf = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = inf

# 创建父节点散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

# 记录处理过的节点
processed = []


def find_lowest_cost_node(costs):
    """找到还未被处理过的最低开销节点。"""
    lowest_cost = inf
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


# 狄克斯特拉算法
while True:
    # 1. 寻找最小开销节点，获得最小开销
    lowest_cost_node = find_lowest_cost_node(costs)
    if lowest_cost_node is None:
        break
    lowest_cost = costs[lowest_cost_node]
    # 2. 找到最小开销节点的邻居
    neighbors = graph[lowest_cost_node]
    # 3. 计算到每个邻居的开销
    for neighbor, neighbor_cost in neighbors.items():
        to_neighbor_cost = lowest_cost + neighbor_cost
        # 4. 如果到邻居的开销比开销表中存储的开销低，
        #    更新最低开销，并设置邻居的父节点为当前最小开销节点
        if to_neighbor_cost < costs[neighbor]:
            costs[neighbor] = to_neighbor_cost
            parents[neighbor] = lowest_cost_node
    # 5. 追加已处理节点列表
    processed.append(lowest_cost_node)


def print_lowest_cost_path(parents):
    path = ['end']
    while path[0] != 'start':
        for k, v in parents.items():
            if path[0] == k:
                path.insert(0, v)
    print(' >>> '.join(path))


print_lowest_cost_path(parents)

"""
start >>> b >>> a >>> end
"""
