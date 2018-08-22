import networkx as nx
from plot import *
from analyze import *
from init import *
import numpy as np

global d
global w
global d

# values for the payoff matrix
a = .1 # benefit from E > E (agreementCoef)
b = 1 # gain from converting N>E (conversionCoef)
# d = .01 # delta (conversationCoef)
c = 2

# payoff matrix of interactions
global Payoff

#probability of message getting through
global Censorship


# Global Constants
NEUTRAL = 2
PASSIVE = 1
EXTREMIST = 0

# return a strategy based on probabilities
def getProbStrategy(G, stratProbs):
    # decision number and temp tracker
    decision = np.random.uniform(0,1, 1)
    total = 0

    for node,probability in stratProbs.items():
        # new total
        total += probability

        # if this is the selected solution
        if decision <= total:
            return(G.nodes[node]['type'])

    return NEUTRAL

def initializeFitness(population):
    for node,d in list(population.nodes(data=True)):
        d['fitness'] = calculateFitness(population, node)

# return deterministic strategy
def getDetStrategy(G, stratProbs):
    max = -1000
    index = 0

    for node,probability in stratProbs.items():
        if (probability > max):
            max = probability
            index = node

    return G.nodes[index]['type']

def calculateFitness(G, node):
    global Payoff
    global Censorship
    #initialize fitness to 0
    fitness = 0

    #iterate over all edges for the node
    for u,v in G.edges(node):
        # calculate the fitness it gets from each node
        nodeType = G.nodes[u]['type']
        neighborType = G.nodes[v]['type']
        fitness += Payoff[nodeType][neighborType] * Censorship[nodeType][neighborType]#* G[u][v]['weight']

    # return the fitness
    return fitness


def getNormalizedFitness(G, node):
    if (G.has_node(node)):
        # empty dict
        neighborFitness = {}

        # loop over, calculate and add into dict
        for u,v in G.edges(node):
            nodeType = G.nodes[u]['type']
            neighborType = G.nodes[v]['type']
            neighborFitness[v] = calculateFitness(G, v) * Censorship[nodeType][neighborType] #G[u][v]['weight']

        # get total fitness
        totalFit = max(sum(neighborFitness.values()),.1) #protect against 0

        # normalize and return
        return {k: v / totalFit for k, v in neighborFitness.items()}
    else:
        return {}

def updateFitness(G, node, strategy):
    # loop over, calculate and add into dict
    for u,v in G.edges(node):
        G.nodes[v]['fitness'] = calculateFitness(G, v)

    # then update itself
    G.nodes[node]['fitness'] = calculateFitness(G, node)

def runSimulation(G, max):
    # run simulation, for i time clicks, plotting at pos
    i = 0

    # initialize the fitness for the nodes in the population
    initializeFitness(G)

    pos = nx.spring_layout(G)

    plt.ion()

    while (i < max):
        # avgFitnessByPopulation(G)
        #pick random node inside the graph
        node = np.random.randint(0,len(G)-1)
        i += 1

        # if extremist, probability of removal
        if (G.nodes[node]['type'] == EXTREMIST and (np.random.uniform(0,1, 1)) < w):
            G.nodes[node]['type'] = NEUTRAL

        # get the normalized fitness to pick the probabilistic strategy
        neighborFitness = getNormalizedFitness(G, node)

        # based on the probabilities, get a new strategy
        newStrategy = getDetStrategy(G, neighborFitness)

        # if need to update strategy
        if (newStrategy != G.nodes[node]['type']):
            G.nodes[node]['type'] = newStrategy
            updateFitness(G, node, newStrategy)

        # plot results
        # visualize(G, pos)

    #return the final score of the population
    return scoreFinalPopulation(G)

def runSimulations(max):
    global Payoff
    global w
    global Censorship

    censorshipRuns = 20
    welfareRuns = 20
    trials = 10
    data = np.zeros((censorshipRuns,welfareRuns))

    # iterate over different dimensions
    for censorship in range(censorshipRuns):
        for j in range(welfareRuns):
            #initialize parameters for the run
            d = j*0.005
            w = .05 * censorship
            print(w,d)

            Payoff = [[a ,b, -1 * c],[b, d, d],[d, d, d]]
            Censorship = [[1 ,w, w],[w, 1, 1],[w, 1, 1]]

            results = []

            #iterate and save the data
            for i in range(trials):
                results.append(runSimulation(initializePopulation(), max))

            # save the result
            data[censorship][j] = sum(results)/len(results)

    return data
