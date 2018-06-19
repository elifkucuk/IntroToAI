def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    listVisited=[]
    queue=util.Queue()
    di=Directions.NORTH
    queue.push(problem.getStartState())
    """Because I'm pushing a tuple into stack in the start I parted this part from the big loop"""
    start=queue.pop()
    listVisited.append(start)
    startSuccessors=problem.getSuccessors(start)
    
    for successor in startSuccessors:
        direction=successor[1]
        if direction is 'South':
            di=Directions.SOUTH
        elif direction is 'West':
            di=Directions.WEST
        elif direction is 'East':
            di=Directions.EAST
        elif direction is 'North':
            di=Directions.NORTH
        path=[]
        path.append(di)
        queueItem=(successor[0], path, successor[2])
        queue.push(queueItem)
    """ from this point on every thing in the big loop"""
    while not queue.isEmpty():
        node=queue.pop()
        pos=node[0]
        print "Pos is",pos
        path=node[1]
        cost=node[2]
        if problem.isGoalState(pos):
            print "Cost is ", cost
            return path
        listVisited.append(pos)
        successors=problem.getSuccessors(pos)
        for successor in successors:
            position=successor[0]
            direction=successor[1]
            additionalCost=successor[2]
            if position not in listVisited:
                if direction is 'South':
                    di=Directions.SOUTH
                elif direction is 'West':
                    di=Directions.WEST
                elif direction is 'East':
                    di=Directions.EAST
                elif direction is 'North':
                    di=Directions.NORTH
                newPath=[]
                newPath=path+[di];
                cumCost=cost+additionalCost
                queueItem=(successor[0], newPath, cumCost)
                queue.push(queueItem)
    util.raiseNotDefined()
