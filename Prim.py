import heapq

def prim(graph, start=0):
    n = len(graph)
    visited = [False] * n
    mst = []
    total_weight = 0
    pq = []

    # 从起点加入堆
    visited[start] = True
    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq:
        w, u, v = heapq.heappop(pq)
        if visited[v]:
            continue
        # 加入 MST
        visited[v] = True
        mst.append((u, v, w))
        total_weight += w

        # 把 v 的邻边加入堆
        for to, weight in graph[v]:
            if not visited[to]:
                heapq.heappush(pq, (weight, v, to))

    return mst, total_weight
