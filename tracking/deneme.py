
import itertools
import random
numParticles=19
legalPos=[(1,2), (3,4), (4,5)]
listOfParticles=[]
num=1
##for x in range(0, numParticles):
##    if (x+1)%(len(legalPos))==0:
##        print "x", x
##        for pos in legalPos:
##            listOfParticles.append(pos)
##remainder=numParticles%len(legalPos)
##for i in range(0, remainder):
##    if i<len(legalPos):
##        listOfParticles.append(legalPos[i])
##    else:
##        listOfParticles.append(legalPos[0])
##    
##        
##print listOfParticles


##iterListC=itertools.combinations(legalPos, 2)
##
##iterListP=itertools.product(legalPos,legalPos)
##
##print "iterListC", list(iterListC)
##
###print "iterListP", list(iterListP)
##
##a=range(9)
##
##b=list(iterListP)
##
##random.shuffle(b)
##
##print "random" , b

numGhosts=3
legalMulPos=legalPos

for i in range(numGhosts-1):
    iterLegalPos=itertools.product(legalMulPos,legalPos)
    legalMulPos=list(iterLegalPos)

print legalMulPos
    


