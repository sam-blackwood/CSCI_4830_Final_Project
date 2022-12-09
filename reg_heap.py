from heapq import heappush, heappop, heapify 


'''
This is a wrapped class over the builtin python binary heap (called heapq) 
to match all of the methods present in fib_heap.py, so that we could use the same
runner methods to compare the performance of the two heaps on Dijkstra's.
'''

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
        # Find index of the old (value, key)/(priority, node#) pair in our heap 
        index = self.heap.index((self.get_value(key), key))

        #Set the value of that index to our new (value, key) pair
        self.heap[index] = (value, key)

        #Builtin method for re-organizing the heap to have prioper priorities
        heapify(self.heap)
               
        self.nodes[key] = value
