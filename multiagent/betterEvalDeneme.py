def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    value=10
    pacmanPos=currentGameState.getPacmanPosition()
    capsuleList=currentGameState.getCapsules()
    ghostPositions=currentGameState.getGhostPositions()   
    foodList=currentGameState.getFood().asList()
    capsuleList=currentGameState.getCapsules()
    closestFoodDistance=0
    averageFoodDistance=0
    ghostStates = currentGameState.getGhostStates()
    numberGhost=len(ghostStates)
    newScaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    scaredPos=[]
    notScaredPos=[]
    scaredGhostDistances=[]
    avgScared=0
    braveGhostDistances=[]
    avgBrave=0
    closestCapsule=0
    wClosestFood=4
    wAvgFood=2
    wScared=4
    wBrave=3
    wCapsule=2
    capsuleValue=0
    scaredValue=0
    braveValue=0
    closestValue=0
    foodValu=0
    capsuleDistances=[manhattanDistance(pacmanPos, pos) for pos in capsuleList]
    if capsuleDistances:
        closestCapsule=min(capsuleDistances)
        capsuleValue=(wCapsule*(1/(closestCapsule+0.0001)))
        print "capsule", capsuleValue
    i=0
    allScared=False
    for scaredTime in newScaredTimes:
        if scaredTime>0:
            allScared=True
    if not allScared:
    if notScaredPos:
        if numberGhost==1:
            braveDist=manhattanDistance(pacmanPos,notScaredPos)
            braveValue=wBrave*(1-(1/(braveDist+0.0001)))
            value+=braveValue
            print "braveValue", braveValue
        else:
            braveGhostDistances=[manhattanDistance(pacmanPos,pos) for pos in notScaredPos]
            avgBrave=sum(braveGhostDistances)/len(braveGhostDistances)
            value+=wBrave*(1-(1/(avgBrave+0.0001)))
    if pacmanPos in ghostPositions:
        print "-200"
        value+=-200
    elif currentGameState.isWin():
        value+=float('inf')
    else:
        foodDistances=[manhattanDistance(pacmanPos,food) for food in foodList]
        closestFoodDistance=min(foodDistances)
        closestValue=(wClosestFood*(1/(closestFoodDistance+0.0001)))
        value+=closestValue
        averageFoodDistance=sum(foodDistances)/len(foodDistances)
        pushEat=-(5*len(foodDistances))
        print "pushEat", pushEat
        value+=pushEat
        foodValu=wAvgFood*(1/(averageFoodDistance+0.0001))
        value+=foodValu
        print "closestValue", closestValue
        print "foodValu", foodValu
        print "value", value
        print "\n \n"
    return value
    #util.raiseNotDefined()
