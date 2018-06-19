# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    listVisited=[]
    stack=util.Stack()
    start=problem.getStartState()
    listVisited.append(start)
    startSuccessors=problem.getSuccessors(start)
    for successor in startSuccessors:
        direction=successor[1]
        path=[]
        path.append(direction)
        stackItem=(successor[0], path, successor[2])
        stack.push(stackItem)
    """ from this point on every thing in the big loop"""
    while not stack.isEmpty():
        node=stack.pop()
        pos=node[0]
        path=node[1]
        cost=node[2]
        if pos not in listVisited:
            listVisited.append(pos)
            if problem.isGoalState(pos):
                return path
            else:
                successors=problem.getSuccessors(pos)
                for successor in successors:
                    position=successor[0]
                    direction=successor[1]
                    additionalCost=successor[2]
                    if position not in listVisited:
                        newPath=[]
                        newPath=path+[direction]
                        cumCost=cost+additionalCost
                        stackItem=(successor[0], newPath, cumCost)
                        stack.push(stackItem)
                
    
    """   util.raiseNotDefined()"""

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    listVisited=[]
    queue=util.Queue()
    listVisited.append(problem.getStartState())
    startSuccessors=problem.getSuccessors(problem.getStartState())   
    for successor in startSuccessors:
        direction=successor[1]
        path=[]
        path.append(direction)
        queueItem=(successor[0], path, successor[2])
        queue.push(queueItem)
    """ from this point on every thing in the big loop"""
    while not queue.isEmpty():
        node=queue.pop()
        pos=node[0]
        path=node[1]
        cost=node[2]
        if pos not in listVisited:
            listVisited.append(pos)
            if problem.isGoalState(pos):
                print "Cost is", cost
                return path
            else:
                successors=problem.getSuccessors(pos)
                for successor in successors:
                    position=successor[0]
                    direction=successor[1]
                    additionalCost=successor[2]
                    if position not in listVisited:
                        newPath=[]
                        newPath=path+[direction];
                        cumCost=cost+additionalCost
                        queueItem=(successor[0], newPath, cumCost)
                        queue.push(queueItem)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    listVisited=[]
    priorityQueue=util.PriorityQueue()
    """Because I'm pushing a tuple into stack in the start I parted this part from the big loop"""
    start=problem.getStartState()
    listVisited.append(start)
    startSuccessors=problem.getSuccessors(start)   
    for successor in startSuccessors:
        direction=successor[1]
        path=[]
        path.append(direction)
        queueItem=(successor[0], path, successor[2])
        priorityQueue.push(queueItem, successor[2])
    """ from this point on every thing in the big loop"""
    while not priorityQueue.isEmpty():
        node=priorityQueue.pop()
        pos=node[0]
        path=node[1]
        cost=node[2]
        if pos not in listVisited:
            listVisited.append(pos)
            if problem.isGoalState(pos):
                return path
            else:
                listVisited.append(pos)
                successors=problem.getSuccessors(pos)
                for successor in successors:
                    position=successor[0]
                    direction=successor[1]
                    additionalCost=successor[2]
                    if position not in listVisited:
                        newPath=[]
                        newPath=path+[direction];
                        cumCost=cost+additionalCost
                        queueItem=(successor[0], newPath, cumCost)
                        priorityQueue.push(queueItem, cumCost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    listVisited=[]
    priorityQueue=util.PriorityQueue()
    heur=heuristic(problem.getStartState(), problem)
    f=heur+0
    """Because I'm pushing a tuple into stack in the start I parted this part from the big loop"""
    start=problem.getStartState()
    listVisited.append(start)
    startSuccessors=problem.getSuccessors(start)   
    for successor in startSuccessors:
        direction=successor[1]
        path=[]
        path.append(direction)
        queueItem=(successor[0], path, successor[2])
        heur=heuristic(successor[0], problem)
        f=successor[2]+heur
        priorityQueue.push(queueItem, f)
    """ from this point on every thing in the big loop"""
    while not priorityQueue.isEmpty():
        node=priorityQueue.pop()
        pos=node[0]
        path=node[1]
        cost=node[2]
        if pos not in listVisited:
            if problem.isGoalState(pos):
                return path
            else:
                listVisited.append(pos)
                successors=problem.getSuccessors(pos)
                for successor in successors:
                    position=successor[0]
                    direction=successor[1]
                    additionalCost=successor[2]
                    if position not in listVisited:
                        newPath=[]
                        newPath=path+[direction];
                        heur=heuristic(pos, problem)
                        cumCost=cost+additionalCost
                        f=heur+cumCost
                        queueItem=(successor[0], newPath, cumCost)
                        priorityQueue.push(queueItem, f)
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
