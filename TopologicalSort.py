import Graph
def topological_sort(graph):
    visited=set()
    stack=[]
    def dfs(node):
        visited.add(node)
        for neighbor in graph.get_neighbors():
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    for node in graph.adj_list:
        if node not in visited:
            dfs(node)
    return stack.reverse()