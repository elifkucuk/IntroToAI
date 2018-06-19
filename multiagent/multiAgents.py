# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util


from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        numberGhost=len(newGhostStates)
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        """ Use getCapsules
            asList method to location of foods as list
            scaredTime: remining time for pacman to eat food
            distance to food?
            distance to ghost?

            """

        "*** YOUR CODE HERE ***"
        value=10
        ghostPosition=successorGameState.getGhostPositions()
        capsulePos=successorGameState.getCapsules()
        oldFoodList=currentGameState.getFood().asList()
        oldCapsule=currentGameState.getCapsules()
        if newPos in oldFoodList:
            value+=1
        if newPos in oldCapsule:
            value+=2
        newFoodList=newFood.asList()
        #find distances to all foods and take the closest foods choose from them arbitraryly
        distancesToAllFoods=[manhattanDistance(newPos, food) for food in newFoodList if food!=newPos]
        closestDistance=0
        totalDistanceToAllFoods=0
        if len(distancesToAllFoods)>0:
            closestDistance=min(distancesToAllFoods)
            totalDistanceToAllFoods=sum(distancesToAllFoods)/len(distancesToAllFoods)
        distancesToGhost=[manhattanDistance(newPos, ghost) for ghost in ghostPosition]
        distanceToGhosts=sum(distancesToGhost)/len(distancesToGhost)
        wClosestFood=0.4
        wDistanceToGhost=0.4
        wTotalDistanceToAllFoods=0.2
        wCapsuleDistance=0.1
        i=0
        allScared=False
        for scaredTime in newScaredTimes:
            if scaredTime>0:
                allScared=True
        if not allScared:
            if len(capsulePos)==0:
                value=value+wClosestFood*(1/(closestDistance+0.0001))+wTotalDistanceToAllFoods*(1/(totalDistanceToAllFoods+0.0001))+wDistanceToGhost*(1-(1/(distanceToGhosts+0.0001)))
            else:
                capsuleDist=manhattanDistance(newPos, capsulePos[0])
                value=value+wClosestFood*(1/(closestDistance+0.0001))+wTotalDistanceToAllFoods*(1/(totalDistanceToAllFoods+0.0001))+wDistanceToGhost*(1-(1/(distanceToGhosts+0.0001)))+wCapsuleDistance*(1/(capsuleDist+0.001))
        else:
            wDistanceToGhost=0.2
            value=value+wClosestFood*(1/(closestDistance+0.0001))+wTotalDistanceToAllFoods*(1/(totalDistanceToAllFoods+0.0001))+wDistanceToGhost*(1/(distanceToGhosts+0.0001))
        #print value
        return value
        #return successorGameState.()
    
    


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.alpha=-float('inf')
        self.betha=float('inf')



class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def value(self, gameState, agentIndex, depth):
        numAgents=gameState.getNumAgents()
        if gameState.isWin() or gameState.isLose():
            v=self.evaluationFunction(gameState)
        elif agentIndex==(numAgents-1):
            v=self.maxValue(gameState, depth)
        else:
            agentIndex+=1
            v=self.minValue(gameState, agentIndex,depth)
        return v

    def maxValue(self, gameState, depth):
        if depth==self.depth:
            v=self.evaluationFunction(gameState)
            return v
        depth+=1
        v=-float('inf')
        listOfActions=gameState.getLegalActions(0)
        for action in listOfActions:
            successor=gameState.generateSuccessor(0,action)
            v=max(v, self.value(successor,0,depth))
        return v
        

    def minValue(self, gameState, agentIndex, depth):
        v=float('inf')
        listOfActions=gameState.getLegalActions(agentIndex)
        for action in listOfActions:
            successor=gameState.generateSuccessor(agentIndex,action)
            v=min(v,self.value(successor, agentIndex, depth))
        return v
        
        
    def getBestAction(self, gameState):
        listOfActions=gameState.getLegalActions(0)
        v=-float('inf')
        best=-float('inf')
        bestAction=Directions.STOP
        for action in listOfActions:
            successor=gameState.generateSuccessor(0,action)
            if successor.isWin() or successor.isLose():
                v=self.evaluationFunction(successor)
            else:
                v=max(v, self.minValue(successor, 1, 1))
            if v>best:
                best=v
                bestAction=action
        return bestAction
    
                
    
        
    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        action=self.getBestAction(gameState)
        return action

        #util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def value(self, gameState,v, agentIndex, depth, alpha, betha):
        numAgents=gameState.getNumAgents()
        if gameState.isWin() or gameState.isLose():
            v=self.evaluationFunction(gameState)
        elif agentIndex==(numAgents-1):
            v=self.maxValue(gameState,v, depth, alpha, betha)
        else:
            agentIndex+=1
            v=self.minValue(gameState,v, agentIndex,depth, False, alpha, betha)
        return v

    def maxValue(self, gameState,v, depth, alpha, betha):
        if depth==self.depth:
            v=self.evaluationFunction(gameState)
            return v
        depth+=1
        v=-float('inf')
        listOfActions=gameState.getLegalActions(0)
        for action in listOfActions:
            successor=gameState.generateSuccessor(0,action)
            v=max(v, self.value(successor,v,0,depth, alpha, betha))
            if v>betha:
                return v
            alpha=max(alpha,v)
        return v
        

    def minValue(self, gameState, v, agentIndex, depth, first, alpha, betha):
        if first:
            if v>betha:
                return v
            alpha=max(alpha,v)
        v=float('inf')
        listOfActions=gameState.getLegalActions(agentIndex)
        for action in listOfActions:
            successor=gameState.generateSuccessor(agentIndex,action)
            v=min(v,self.value(successor, v, agentIndex, depth, alpha, betha))
            if v<alpha:
                return v
            betha=min(betha,v)
        return v
        
        
    def getBestAction(self, gameState):
        listOfActions=gameState.getLegalActions(0)
        v=-float('inf')
        best=-float('inf')
        bestAction=Directions.STOP
        alpha=-float('inf')
        betha=float('inf')
        for action in listOfActions:
            successor=gameState.generateSuccessor(0,action)
            if successor.isWin() or successor.isLose():
                v=self.evaluationFunction(successor)
            else:
                v=max(v, self.minValue(successor, v, 1, 1, True, alpha, betha))
            if v>best:
                best=v
                bestAction=action
        return bestAction

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        action=self.getBestAction(gameState)
        return action
        #util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def value(self, gameState, agentIndex, depth):
        numAgents=gameState.getNumAgents()
        if gameState.isWin() or gameState.isLose():
            v=self.evaluationFunction(gameState)
        elif agentIndex==(numAgents-1):
            v=self.maxValue(gameState, depth)
        else:
            agentIndex+=1
            v=self.expValue(gameState, agentIndex,depth)
        return v
    def expValue(self, gameState, agentIndex, depth):
        v=0
        listOfActions=gameState.getLegalActions(agentIndex)
        for action in listOfActions:
            successor=gameState.generateSuccessor(agentIndex,action)
            p=1.0/len(listOfActions)
            v+=p*self.value(successor, agentIndex, depth)
        return v
        

    def maxValue(self, gameState, depth):
        if depth==self.depth:
            v=self.evaluationFunction(gameState)
            return v
        depth+=1
        v=-float('inf')
        listOfActions=gameState.getLegalActions(0)
        for action in listOfActions:
            successor=gameState.generateSuccessor(0,action)
            v=max(v, self.value(successor,0,depth))
        return v
        

    def minValue(self, gameState, agentIndex, depth):
        v=float('inf')
        listOfActions=gameState.getLegalActions(agentIndex)
        for action in listOfActions:
            successor=gameState.generateSuccessor(agentIndex,action)
            v=min(v,self.value(successor, agentIndex, depth))
        return v
        
        
    def getBestAction(self, gameState):
        listOfActions=gameState.getLegalActions(0)
        v=-float('inf')
        best=-float('inf')
        bestAction=Directions.STOP
        allActions=[]
        for action in listOfActions:
            if action!=Directions.STOP:
                allActions.append(action)
                listOfActions.remove(action)
        for action in listOfActions:
            allActions.append(action)
        for action in allActions:
            successor=gameState.generateSuccessor(0,action)
            if successor.isWin() or successor.isLose():
                v=self.evaluationFunction(successor)
            else:
                v=max(v, self.expValue(successor, 1, 1))
            if v>best:
                best=v
                bestAction=action
        return bestAction

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        action=self.getBestAction(gameState)
##        print "return action", action
##        print "\n"
        return action
        #util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacmanPos=currentGameState.getPacmanPosition()
    capsuleList=currentGameState.getCapsules()
    ghostPositions=currentGameState.getGhostPositions()
    foodList=currentGameState.getFood().asList()
    if len(foodList)==0:
        return 10000000000
    elif pacmanPos in ghostPositions:
        return -100000000
    value=10
    pacmanPos=currentGameState.getPacmanPosition()
    capsuleList=currentGameState.getCapsules()
    ghostPositions=currentGameState.getGhostPositions()   
    capsuleList=currentGameState.getCapsules()
    closestFoodDistance=0
    averageFoodDistance=0
    ghostStates = currentGameState.getGhostStates()
    numberGhost=len(ghostStates)
    newScaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    ghostDistances=[]
    avgGhost=0
    closestCapsule=0
    wClosestFood=5
    wAvgFood=4
    wGhost=4
    wCapsule=3
    capsuleValue=0
    ghostValue=0
    closestValue=0
    foodValu=0
    pushEat=0
    capsuleDistances=[manhattanDistance(pacmanPos, pos) for pos in capsuleList]
    
    """ Capsule distance value calculated"""
    if capsuleDistances:
        closestCapsule=min(capsuleDistances)
        capsuleValue=(wCapsule*(1/(closestCapsule+0.0001)))
    """ Ghost distances are calculated state are determined """
    ghostDistances=[manhattanDistance(pacmanPos, pos) for pos in ghostPositions]
    avgGhost=sum(ghostDistances)/len(ghostDistances)
    allScared=True
    for scaredTime in newScaredTimes:
        if scaredTime==0:
            allScared=False
    if not allScared:
        ghostValue=wGhost*(1-(1/(avgGhost+0.0001)))
        if pacmanPos in ghostPositions:
            value+=-3000000
    else:
        wGhost=6
        ghostValue=wGhost*(1/(avgGhost+0.0001))
    """ Check if current state is win"""
    if currentGameState.isWin():
        value+=float('inf')

    """ Food distances are calculated """
    foodDistances=[manhattanDistance(pacmanPos,food) for food in foodList]
    if foodDistances:
        closestFoodDistance=min(foodDistances)
        closestValue=(wClosestFood*(1/(closestFoodDistance+0.0001)))       
        averageFoodDistance=sum(foodDistances)/len(foodDistances)
        pushEat=-6*(len(foodDistances)+0.0001)
        foodValu=wAvgFood*(1/(averageFoodDistance+0.0001))
    """ """
    
    value+=pushEat
    value+=closestValue
    value+=foodValu
    value+=capsuleValue
    value+=ghostValue
    value+=-20*(len(capsuleList)+0.0001)
    return value
    #util.raiseNotDefined()


def manhattanDistance(position, position2, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = position2
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

# Abbreviation
better = betterEvaluationFunction

