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
            print "rootWin", v
            return v
        elif depth==self.depth:
            print "rootDepth",v
            v=self.evaluationFunction(gameState)
            return v
        else:
            depth+=1
            v=-float('inf')
            listOfActions=gameState.getLegalActions(agentIndex)
            listOfSuccessors=[gameState.generateSuccessor(agentIndex,action) for action in listOfActions]
            for successor in listOfSuccessors:
                mam=self.value(successor,v, 1, depth)
                print "mam", mam
                v=max(v,mam)
                print "vmax", v
            return v
    def minValue(self, gameState, v, agentIndex, depth):
        print "MinAgentIndex", agentIndex
        numAgents=gameState.getNumAgents()
        if agentIndex==numAgents-1:
            agentIndex=0
        else:
            agentIndex+=1
        if gameState.isWin() or gameState.isLose(): 
            v=self.evaluationFunction(gameState)
            print "rootWin", v
            return v
        elif depth==self.depth:
            print "rootDepth",v
            v=self.evaluationFunction(gameState)
            return v
        else:
            v=float('inf')
            listOfActions=gameState.getLegalActions(agentIndex)
            listOfSuccessors=[gameState.generateSuccessor(agentIndex,action) for action in listOfActions]
            for successor in listOfSuccessors:
                hom=self.value(successor, v, agentIndex, depth)
                print "hom", hom
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
            pre=val
            print "Pre",pre
            val=self.maxValue(successor, val, 0, -1)
            print "Val", val
            if val>=pre:
                best=val
                act=action
        return act
