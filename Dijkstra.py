import heapq
import Graph
def Dijkstra_ShortestPath(graph, a, b):
    n = len(graph)
    dis = [float("inf")] * n
    dis[a] = 0
    pq = [(0, a)]

    while pq:
        d, u = heapq.heappop(pq)
        if u == b:
            return d
        if d > dis[u]:
            continue
        for v, w in graph[u]:
            if dis[v] > d + w:
                dis[v] = d + w
                heapq.heappush(pq, (dis[v], v))

    return float("inf")
def dijkstra_ShortestPath(graph: Graph, source):
    n = len(graph)
    d = [float('inf')] * n
    pi = [None] * n
    s = [0] * n
    pq = []

    d[source] = 0
    heapq.heappush(pq, (0, source))
    while pq:
        d_u, u = heapq.heappop(pq)
        if s[u] == 1:
            continue
        s[u] = 1
        for vertex, w_uv in graph[u]:  # 假设 graph[u] = [(v, weight), ...]
            if s[vertex] != 1 and d[vertex] > d[u] + w_uv:
                d[vertex] = d[u] + w_uv
                pi[vertex] = u
                heapq.heappush(pq, (d[vertex], vertex))

    return d, pi
def get_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    path.reverse()
    return path
