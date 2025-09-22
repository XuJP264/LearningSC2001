from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        cur = queue.popleft()   # 从队头取
        if cur not in visited:
            print(cur, end=" ")
            visited.add(cur)
            for neighbor in graph.get_neighbors(cur):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited
