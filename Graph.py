class Graph:
    def __init__(self):
        # 用字典存储：key 是顶点，value 是邻居列表
        self.adj_list = {}

    def add_vertex(self, v):
        """添加一个顶点"""
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        """添加一条无向边 u-v"""
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def add_directed_edge(self, u, v):
        """添加一条有向边 u->v"""
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        self.adj_list[u].append(v)

    def get_neighbors(self, v):
        """返回顶点 v 的邻居"""
        return self.adj_list.get(v, [])

    def show(self):
        """打印邻接表"""
        for v in self.adj_list:
            print(v, "->", self.adj_list[v])
