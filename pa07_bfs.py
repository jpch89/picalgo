from collections import deque

# 构建图
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def is_mango_seller(person):
    """判断一个人是否为芒果供应商。"""
    # return True if person[-1] == 'm' else False
    # 更好的写法：
    return person[-1] == 'm'


def search_mango_seller(name):
    """寻找一个人的关系网中是否有芒果供应商。"""
    q = deque(graph[name])
    searched = []

    while q:
        person = q.popleft()
        if person not in searched:
            if is_mango_seller(person):
                return person
            else:
                q.extend(graph[person])
                searched.append(person)

    return None


if __name__ == '__main__':
    print(search_mango_seller('you'))
