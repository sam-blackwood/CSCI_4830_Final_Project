# Fibonacci Heap in python

#mainly used this source for extract min and deleting min
# https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf

#some inspiration from this source
# https://www.programiz.com/dsa/fibonacci-heap

import math

# Creating fibonacci tree

class Node:
    def __init__(self, value, key):
        self.value = value
        self.child = []
        self.order = 0
        self.key = key

    # Adding tree at the end of the tree
    def add_at_end(self, t):
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

    def insert_node(self, value, key):
        new_node = Node(value, key)
        self.all_nodes[key] = new_node
        self.nodes.append(new_node)
        if (self.min == None or value < self.min.value):
            self.min = new_node
        self.count = self.count + 1

    def get_min(self):
        if self.min == None:
            return None
        return self.min.value, self.min.key

    #get min value, then delete it
    def extract_min(self):
        smallest = self.min
        if smallest != None:
            self.all_nodes.pop(smallest.key)
            #taking all nodes from min node append to root list
            for child in smallest.child:
                self.nodes.append(child)
            self.nodes.remove(smallest)
            if self.nodes == []:
                self.min = None
            else:
                self.min = self.nodes[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.value, smallest.key

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

