# Fibonacci Heap in python

#mainly used this source for extract min and deleting min
# https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf

#some inspiration from this source
# https://www.programiz.com/dsa/fibonacci-heap

import math

class Node:
    def __init__(self, value, key):
        self.value = value
        self.child = []
        self.order = 0
        self.key = key
        self.parent = None
        self.marked = False

    # Adding node to child list
    def add_at_end(self, t):
        t.parent = self
        self.child.append(t)
        self.order = self.order + 1


class FibonacciHeap:
    def __init__(self):
        #this is the root list
        self.nodes = []
        self.min = None
        #this is how many nodes are in root list
        self.count = 0
        self.all_nodes = {}


    def get_value(self, key):
        return self.all_nodes[key].value

    def insert_node(self, key, value):
        new_node = Node(value, key)
        self.all_nodes[key] = new_node
        self.nodes.append(new_node)
        if (self.min == None or value < self.min.value):
            self.min = new_node
        self.count = self.count + 1

    def get_min(self):
        if self.min == None:
            return None
        return self.min.key, self.min.value

    #get min value, then delete it
    def extract_min(self):
        smallest = self.min
        if smallest != None:
            self.all_nodes.pop(smallest.key)
            #taking all nodes from min node append to root list
            for child in smallest.child:
                self.nodes.append(child)
                child.parent = None
            self.nodes.remove(smallest)
            if self.nodes == []:
                self.min = None
            else:
                self.min = self.nodes[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key, smallest.value 


    def decrease_key(self, key, value):
        node = self.all_nodes[key]
        node.value = value
        node_parent = node.parent
        if node_parent != None and node.value < node_parent.value:
            self.cut(node)
            self.cascading_cut(node_parent)
        if node.value < self.min.value:
            self.min = node

    def cut(self, node):
        node.parent.child.remove(node)
        node.parent.order = node.parent.order - 1
        self.nodes.append(node)
        node.parent = None
        node.marked = False
    
    def cascading_cut(self, node):
        node_parent = node.parent
        if node_parent != None:
            if node.marked == False:
                node.marked = True
            else:
                self.cut(node)
                self.cascading_cut(node_parent)


    #consolidate tree so every node in root list has different rank
    def consolidate(self):
        #create an array of size 2log of root list size
        #found this sizing here https://ac.informatik.uni-freiburg.de/lak_teaching/ws07_08/algotheo/Slides/08_fibonacci_heaps.pdf
        aux = ((2 * math.ceil(math.log(self.count))) ) * [None]

        #traverse the root list everytime we get to a node we will remove it from the root list and insert it into the aux array
        while self.nodes != []:
            x = self.nodes[0]
            order = x.order
            self.nodes.remove(x)
            while aux[order] != None:
                y = aux[order]

                #make sure x is smaller than y
                #x goes in root list
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.min = None

        self.nodes == []
        #make root list
        for k in aux:
            if k != None:
                self.nodes.append(k)
                #setting min value
                if (self.min == None or k.value < self.min.value):
                    self.min = k

