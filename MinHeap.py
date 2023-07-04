class MHNode:
    def __init__(self, ride, rbt, min_heap_index):
        self.ride = ride
        self.rbTree = rbt
        self.min_heap_index = min_heap_index

class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0

    #inserts a new node into the heap
    def insert(self, ele):
        self.heap_list.append(ele)
        self.curr_size += 1
        self.heapifyUp(self.curr_size)

    #swaps the values of the two nodes
    def swap(self, ind1, ind2):
        temp = self.heap_list[ind1]
        self.heap_list[ind1] = self.heap_list[ind2]
        self.heap_list[ind2] = temp
        self.heap_list[ind1].min_heap_index = ind1
        self.heap_list[ind2].min_heap_index = ind2

    #gets the minimum value from the heap
    def getMin(self, u):
        if (u * 2) + 1 > self.curr_size:
            return u * 2
        else:
            if self.heap_list[u * 2].ride.lessThan(self.heap_list[(u * 2) + 1].ride):
                return u * 2
            else:
                return (u * 2) + 1

    #updates the value of the node
    def update(self, u, v):
        node = self.heap_list[u]
        node.ride.tripDuration = v
        if u == 1:
            self.heapifyDown(u)
        elif self.heap_list[u // 2].ride.lessThan(self.heap_list[u].ride):
            self.heapifyDown(u)
        else:
            self.heapifyUp(u)

    def delete(self, u):

        self.swap(u, self.curr_size)
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapifyDown(u)

    def pop(self):

        if len(self.heap_list) == 1:
            return 'No Rides Available'

        root = self.heap_list[1]

        self.swap(1, self.curr_size)
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapifyDown(1)

        return root
    
    #heapify down
    def heapifyDown(self, u):
        while (u * 2) <= self.curr_size:
            ind = self.getMin(u)
            if not self.heap_list[u].ride.lessThan(self.heap_list[ind].ride):
                self.swap(u, ind)
            u = ind

    
    #heapify up
    def heapifyUp(self, u):
        while (u // 2) > 0:
            if self.heap_list[u].ride.lessThan(self.heap_list[u // 2].ride):
                self.swap(u, (u // 2))
            else:
                break
            u = u // 2