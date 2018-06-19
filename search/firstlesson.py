import util
stack=["South", "West"]
di="South"
newStack=[]
newStack=stack+[di]
print newStack
pos=(5, 3)
successors=[((5, 4), 'South', 1), ((4, 5), 'West', 1)]
fruitPrices={'apple':2.00, 'oranges':1.50, 'pears':1.75}

    
priorityQueue=util.PriorityQueue()


priorityQueue.push( ((4, 5), ('South1', 'West')), 1)

priorityQueue.push( ((2, 5), ('North3', 'West')),3)

priorityQueue.push( ((3, 5), ('South2', 'West')), 2)

priorityQueue.push( ((3, 5), ('South4', 'West')), 4)

entry=priorityQueue.pop()

entry2=priorityQueue.pop()

entry3=priorityQueue.pop()

entry4=priorityQueue.pop()

print entry

print entry2

print entry3

print entry4

state2=[(4, 5), [(1, 1), (1, 6), (6, 1), (6, 6)]]
x,y=state2[0]

state2[1][0]=(0,0)


state=(1,2)

state3=[(1,3), [(2,3), (3,4)]]

##
##def statechange(state):
##    state=(2,3)
##    print state;
##statechange(state)
##print "State is", state
##
##class deneme:
##    def __init__(self):
##        self.state=[(4,5), [(3,5),(2,4)]]
##    def getState(self):
##        return self.state
##    def setState(self):
##        self.state[1][0]=(2,4)


class StateSpace:

    def __init__(self, startPosition, corners):
        self.position=startPosition
        self.cornerState=corners
    def getPos(self):
        return self.position
    def getCornerState(self):
        return self.cornerState

newState=((3,4), [(0,0), (0,0), (1,0), (0,0)])
isGoal=True
corners=newState[1]
for corner in corners:
    if corner!=(0,0):
        isGoal=False
print isGoal

lst=[]
lst.append(2)
lst.append(1)
lst.sort()
print lst
lst.reverse()
lst.pop()
lst.reverse()
print lst

foodlist=[0,1,2,3,4]
eleman=[]
for food in foodlist:
    foo=food
    print foodlist
    foodlist.reverse()
    foodlist.pop()
    foodlist.reverse()
    
print foodlist

class Edge:
    def __init__(self, point1, point2, distance):
        self.point1=point1
        self.point2=point2
        self.distance=distance
edge=Edge((0,0),(1,0),3)
print edge.point1

import util

class Edge:
    def __init__(self, point1, point2, distance):
        self.point1=point1
        self.point2=point2
        self.distance=distance

edge=Edge((1,1),(2,2),2)
edge3=Edge((1,1),(2,2),3)

queue=util.PriorityQueue()
queue.push(edge,1)
queue.push(edge,2)
ed=queue.pop()
ed2=queue.pop()
ed3=queue.pop()
