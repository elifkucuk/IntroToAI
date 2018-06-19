
class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function
    """

    def __init__(self, startingGameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = [(1,1), (1,top), (right, 1), (right, top)]
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print 'Warning: no food in corner ' + str(corner)
        self._expanded = 0 # DO NOT CHANGE; Number of search nodes expanded
        # Please add any code here which you would like to use
        # in initializing the problem
        "*** YOUR CODE HERE ***"
        self.costFn=lambda x: 1
        self.state=[self.startingPosition, self.corners]

    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        "*** YOUR CODE HERE ***"
        return [self.startingPosition, self.corners]
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
        Returns whether this search state is a goal state of the problem.
        """
        "*** YOUR CODE HERE ***"
        isGoal=1
        corner1=state[1][0]
        corner2=state[1][1]
        corner3=state[1][2]
        corner4=state[1][3]
        if corner1==self.corners[0]:
            isGoal=False
        elif corner2==self.corners[1]:
            isGoal=False
        elif corner3==self.corners[2]:
            isGoal=False
        elif corner4==self.corners[3]:
            isGoal=False
        return isGoal
        util.raiseNotDefined()
        
            
    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that successor
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            #   x,y = currentPosition
            #   dx, dy = Actions.directionToVector(action)
            #   nextx, nexty = int(x + dx), int(y + dy)
            #   hitsWall = self.walls[nextx][nexty]

            "*** YOUR CODE HERE ***"
            pos=state[0]
            poss=state[1]
            check=[]
            if pos==self.corners[0]:
                check.append((0,0))
            else:
                check.append(poss[0])
            if pos==self.corners[1]:
                check.append((0,0))
            else:
                check.append(poss[1])
            if pos==self.corners[2]:
                check.append((0,0))
            else:
                check.append(poss[2])
            if pos==self.corners[3]:
                check.append((0,0))
            else:
                check.append(poss[3])
            x,y=state[0]
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = [(nextx, nexty), check]
                cost = self.costFn(nextState)
                successors.append( ( nextState, action, cost) )

        self._expanded += 1 # DO NOT CHANGE
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)
