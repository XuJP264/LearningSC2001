parent = []
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(y)] = find(x)

def kruskal(graph):
    global parent
    n = len(graph)
    edge = []

    # 构建边列表
    for i in range(n):
        for v, w in graph[i]:
            edge.append((i, v, w))

    # 按权重升序排序
    sorted_edges = sorted(edge, key=lambda x: x[2])

    parent = [i for i in range(n)]

    remain_edge = n - 1
    i = 0
    mst = []
    total_weight = 0

    while remain_edge > 0 and i < len(sorted_edges):
        cur = sorted_edges[i]
        if find(cur[0]) != find(cur[1]):
            mst.append(cur)
            total_weight += cur[2]
            union(cur[0], cur[1])
            remain_edge -= 1
        i += 1

    return mst, total_weight
