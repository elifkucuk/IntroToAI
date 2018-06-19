def value(self, gameState, v, agentIndex, depth):
        numAgents=gameState.getNumAgents()
        
        if agentIndex==0:
            v=self.maxValue(gameState, v, 0, depth)               
        else:
            v=self.minValue(gameState, v, agentIndex, depth)
        return v           
    def maxValue(self, gameState, v, agentIndex, depth):
        print "MaxagentIndex", agentIndex
        if gameState.isWin() or gameState.isLose(): 
            v=self.evaluationFunction(gameState)
            print "rootWinMax", v
            return v
        elif depth==self.depth:
            print "rootDepthMax",v
            v=self.evaluationFunction(gameState)
            return v
        else:
            v=-float('inf')
            listOfActions=gameState.getLegalActions(agentIndex)
            listOfSuccessors=[gameState.generateSuccessor(agentIndex,action) for action in listOfActions]
            for successor in listOfSuccessors:
                mam=self.value(successor,v, 1, depth)
                v=max(v,mam)
                print "vmax", v
            return v
    def minValue(self, gameState, v, agentIndex, depth):
        print "MinAgentIndex", agentIndex
        if gameState.isWin() or gameState.isLose(): 
            v=self.evaluationFunction(gameState)
            print "rootWinMin", v
            return v
        elif depth==(self.depth):
            print "rootDepthMin",v
            v=self.evaluationFunction(gameState)
            return v
        else:
            numAgents=(gameState.getNumAgents()-1)
            if agentIndex==numAgents-1:
                agentIndex=0
                depth+=1
            else:
                agentIndex+=1
            v=float('inf')
            listOfActions=gameState.getLegalActions(agentIndex)
            listOfSuccessors=[gameState.generateSuccessor(agentIndex,action) for action in listOfActions]
            for successor in listOfSuccessors:
                hom=self.value(successor, v, agentIndex, depth)
                v=min(v,hom)
                print "vmin", v
            return v
    def getBestAction(self, gameState):
        listOfActions=gameState.getLegalActions(0)
        agentIndex=gameState.getNumAgents()-1
        best=0
        act=Directions.STOP
        val=-float('inf')
        for action in listOfActions:
            successor=gameState.generateSuccessor(0, action)
            best=val
            val=max(val, self.minValue(successor, val, 1, 1))
            print "Val", val
            if val>best:
                best=val
                act=action
            print "best", best
            print "act", act
        return act
