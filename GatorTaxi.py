import sys

from RideModel import Ride
from MinHeap import MinHeap, MHNode
from RedBlackTree import RedBlackTree, RBTNode


def addToOutput(ride, message, list):
    file = open("output.txt", "a")
    if ride is None:
        file.write(message + "\n")
    else:
        message = ""
        if not list:
            message += ("(" + str(ride.rideNumber) + "," + str(ride.rideCost) + "," + str(ride.tripDuration) + ")\n")
        else:
            if len(ride) == 0:
                message += "(0,0,0)\n"
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + "),")
                else:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + ")\n")

        file.write(message)
    file.close()

#Operation -1 --- Print one ride
def print(rideNumber, rbt):
    res = rbt.getRide(rideNumber)
    if res is None:
        addToOutput(Ride(0, 0, 0), "", False)
    else:
        addToOutput(res.ride, "", False)

#Operation 2 --- Print all rides within range
def print1(l, h, rbt):
    list = rbt.getRidesInRange(l, h)
    addToOutput(list, "", True)

#Operation 3 - Insert a new ride into the list of rides
def insert(ride, heap, rbt):
    if rbt.getRide(ride.rideNumber) is not None:
        addToOutput(None, "Duplicate RideNumber", False)
        sys.exit(0)
        return
    rbt_node = RBTNode(None, None)
    min_heap_node = MHNode(ride, rbt_node, heap.curr_size + 1)
    heap.insert(min_heap_node)
    rbt.insert(ride, min_heap_node)

#Operation 4 --- Get Next Ride
def getNext(heap, rbt):
    if heap.curr_size != 0:
        popped_node = heap.pop()
        rbt.delete(popped_node.ride.rideNumber)
        addToOutput(popped_node.ride, "", False)
    else:
        addToOutput(None, "No active ride requests", False)

#Operation 5 --- Cancel Ride
def cancel(ride_number, heap, rbt):
    heap_node = rbt.delete(ride_number)
    if heap_node is not None:
        heap.delete(heap_node.min_heap_index)

#Operation 6 --- Update Ride
def update(rideNumber, new_duration, heap, rbt):
    rbt_node = rbt.getRide(rideNumber)
    if rbt_node is None:
        print("")
    elif new_duration <= rbt_node.ride.tripDuration:
        heap.update(rbt_node.min_heap_node.min_heap_index, new_duration)
    elif rbt_node.ride.tripDuration < new_duration <= (2 * rbt_node.ride.tripDuration):
        cancel(rbt_node.ride.rideNumber, heap, rbt)
        insert(Ride(rbt_node.ride.rideNumber, rbt_node.ride.rideCost + 10, new_duration), heap, rbt)
    else:
        cancel(rbt_node.ride.rideNumber, heap, rbt)


if __name__ == "__main__":
    filename = sys.argv[1]
    heap = MinHeap()
    rbt = RedBlackTree()
    file = open("output.txt", "w")
    file.close()
    file = open(filename, "r")
    for s in file.readlines():
        n = []
        for num in s[s.index("(") + 1:s.index(")")].split(","):
            if num != '':
                n.append(int(num))
        if "Insert" in s:
            insert(Ride(n[0], n[1], n[2]), heap, rbt)
        elif "Print" in s:
            if len(n) == 1:
                print(n[0], rbt)
            elif len(n) == 2:
                print1(n[0], n[1], rbt)
        elif "UpdateTrip" in s:
            update(n[0], n[1], heap, rbt)
        elif "GetNextRide" in s:
            getNext(heap, rbt)
        elif "CancelRide" in s:
            cancel(n[0], heap, rbt)