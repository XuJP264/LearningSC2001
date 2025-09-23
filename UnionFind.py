def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return False  # 已经在同一集合
    parent[py] = px  # 把 py 挂到 px 下
    return True       # 合并成功
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 路径压缩
    return parent[x]
