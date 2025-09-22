class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, key):
        """插入一个元素到堆中"""
        self.heap.append(key)
        i = len(self.heap) - 1
        # 向上调整
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def pop(self):
        """弹出堆顶元素（最小值）"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # 把最后一个元素移到堆顶
        self.heapify(0)
        return root

    def heapify(self, i):
        """维护堆的性质，从下标 i 开始"""
        smallest = i
        l, r = self.left(i), self.right(i)

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def peek(self):
        """查看堆顶元素，不删除"""
        return self.heap[0] if self.heap else None

    def size(self):
        """返回堆的大小"""
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
