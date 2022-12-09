from heapq import heappush, heappop, heapify 

class MinHeap:
      
    # Constructor to initialize a heap
    def __init__(self):
        self.nodes = {}
        self.heap = []

    def get_value(self, key):
        return self.nodes[key]

    def insert_node(self, key, value):
        self.nodes[key] = value
        heappush(self.heap, (value, key))

    def get_min(self):
        return self.heap[0][1], self.heap[0][0]

    def extract_min(self):
        ret = heappop(self.heap)
        del self.nodes[ret[1]]
        return ret[1], ret[0]

    def decrease_key(self, key, value):
        self.insert_node(key, value)
