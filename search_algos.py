import math

class SearchNode:
    def __init__(self, state, action=-1, prevNode=None):
        self.state = state
        self.action = action
        self.prevNode = prevNode
        self.totalG = 0 # kustannus alusta nykyiseen tilaan
        self.heuristicCost = 0 # Arvioitu kustannus loppuun
    
def traversePath(node, visitFunc):
    if (node == None):
        return # rekursion loppuehto
    traversePath(node.prevNode, visitFunc)
    visitFunc(node)

def dijkstra(agentState, popBest, isGoalFound, branch):
    # lisää alkutila open listiin
    openList = [SearchNode(agentState)]
    closedList = []
    goaledNode = None

    def isInClosedList(node):
        for n in closedList:
            if(node.state == n.state):
                return True #löytyi
        return False #ei löytynyt

    while len(openList) > 0 and goaledNode == None:
        currentNode = popBest(openList)

        # lisää solmu closed listaan
        closedList.append(currentNode)
        if isGoalFound(currentNode):
            goaledNode = currentNode
            continue

        # Laske seuraavat naapurisolmut
        adjacentNodes = branch(currentNode) # kutsu branch funktiota kanditaattien saamiseksi
        for n in adjacentNodes:
            if(isInClosedList(n)):
                continue
            closedList.append(n)
            openList.append(n)  

    return goaledNode, openList, closedList

def searhPathFindInGrid(initialState, endState, isLegalState, level, actions, popBest):

    # maalifunktio:
    def isGoalFound(node):
        return node.state[0] == endState[0] and node.state[1] == endState[1]   
    
    # Suorittaa annetun actionin nykyisestä tilasta eteenpäin
    def makeAction(currentState, actionId):
        deltaAction = actions[actionId]
        newState = []
        for i in range(len(currentState)):
            newState.append(currentState[i]+deltaAction[i])
        return newState

    # Suorittaa actionin nykyiseen tilaan ja tekee uuden solmun
    def stepAction(prevNode, actionId):
        newState = makeAction(prevNode.state, actionId)
        return SearchNode(newState, actionId, prevNode)

    def vectorLen(vec):
        dotProduct = 0
        for value in vec:
            dotProduct += value*value
        return math.sqrt(dotProduct)

    def sub(v1, v2):
        result = []
        for i in range(len(v1)):
            result.append(v1[i] - v2[i])
        return result

    # branch funktio algoritmille
    def getNextNodes(prevNode):
        NextNodes = []
        for actionId in range(len(actions)):
            newNode = stepAction(prevNode, actionId)
            x = prevNode.state[0]
            y = prevNode.state[1]
            levelCost = level[y][x] + 1
            if(isLegalState(newNode.state)):
                #  G-kustannus on edellisten g plus kustannus yhdelle askeleelle:
                newNode.totalG = prevNode.totalG + levelCost*vectorLen(sub(prevNode.state, newNode.state))
                newNode.heuristicCost = int(vectorLen(sub(newNode.state, endState))) #euklidinen pituus
                NextNodes.append(newNode)
        return NextNodes
    
    return dijkstra(initialState, popBest, isGoalFound, getNextNodes) 

# Leveyssuunnatun haun kustannusfunktio:    
def popBestG(openList):
    # oleta ensimmäinen pienimmäksi
    currentNode = openList[0]
    minIndex = 0
    minG = currentNode.totalG
    for index, item in enumerate(openList):
        itemG = item.totalG
        if( itemG < minG):
            currentNode = item
            minIndex = index
            minG = itemG
    openList.pop(minIndex)
    return currentNode

# Ahneen haun kustannusfunktio:
def popBestH(openList):
    # oleta ensimmäinen pienimmäksi
    currentNode = openList[0]
    minIndex = 0
    minH = currentNode.heuristicCost
    for index, item in enumerate(openList):
        itemH = item.heuristicCost
        if( itemH < minH):
            currentNode = item
            minIndex = index
            minH = itemH
    openList.pop(minIndex)
    return currentNode

# A* haun kustannusfunktio:
k = 1.0
def popBestF(openList):
    # oleta ensimmäinen pienimmäksi
    currentNode = openList[0]
    minIndex = 0
    # F = G + k*H
    minF = currentNode.totalG + k*currentNode.heuristicCost
    for index, item in enumerate(openList):
        itemF = item.totalG + k*item.heuristicCost
        if( itemF < minF):
            currentNode = item
            minIndex = index
            minF = itemF
    openList.pop(minIndex)
    return currentNode

