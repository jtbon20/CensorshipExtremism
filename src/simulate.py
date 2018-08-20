import sys
import networkx as nx
from plot import *
from analyze import *
from numpy import vstack, zeros
import numpy as np

# Global Constants
NEUTRAL = 2
PASSIVE = 1
EXTREMIST = 0

# values for the payoff matrix
a = .1 # benefit from E > E (agreementCoef)
b = 1 # gain from converting N>E (conversionCoef)
c = 5 # cost of revealing views to non-believer  (badRevealCoef )
d = .1 # delta (conversationCoef)

# payoff matrix of interactions
Payoff = [[a ,b, -1 * c],[b, d, d],[-1 * d, d, d]]

def calculateFitness(G, node):
    #initialize fitness to 0
    fitness = 0

    #iterate over all edges for the node
    for u,v in G.edges(node):
        # calculate the fitness it gets from each node
        nodeType = G.nodes[u]['type']
        neighborType = G.nodes[v]['type']
        fitness += Payoff[nodeType][neighborType] * G[u][v]['weight']

    # return the fitness
    return fitness

def getNormalizedFitness(G, node):
    if (G.has_node(node)):
        # empty dict
        neighborFitness = {}

        # loop over, calculate and add into dict
        for u,v in G.edges(node):
            neighborFitness[v] = calculateFitness(G, v) * G[u][v]['weight']

        # get total fitness
        totalFit = sum(neighborFitness.values())

        # normalize and return
        return {k: v / totalFit for k, v in neighborFitness.items()}
    else:
        return {}
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

    return -1

# return deterministic strategy
def getDetStrategy(G, stratProbs):
    max = -1000
    index = 0

    print('************')
    for node,probability in stratProbs.items():
        print(node,probability)
        if (probability > max):
            max = probability
            index = node

    print('returning:', G.nodes[index]['type'])
    return G.nodes[index]['type']

def updateFitness(G, node, strategy, censorProbWeight):
    # loop over, calculate and add into dict
    for u,v in G.edges(node):
        G.nodes[v]['fitness'] = calculateFitness(G, v)
        if (strategy == EXTREMIST):
            G[u][v]['weight'] = censorProbWeight

    # then update itself
    G.nodes[node]['fitness'] = calculateFitness(G, node)

def runSimulation(G, max, censorProbWeight):
    # run simulation, for i time clicks, plotting at pos
    i = 0
    pos = nx.spring_layout(G)

    plt.ion()

    while (i < max):
        avgFitnessByPopulation(G)
        #pick random node inside the graph
        node = np.random.randint(0,len(G)-1)
        i += 1

        # get the normalized fitness to pick the probabilistic strategy
        neighborFitness = getNormalizedFitness(G, node)

        # based on the probabilities, get a new strategy
        newStrategy = getProbStrategy(G, neighborFitness)

        # if need to update strategy
        if (newStrategy != G.nodes[node]['type']):
            G.nodes[node]['type'] = newStrategy
            updateFitness(G, node, newStrategy, censorProbWeight)

        # plot results
        visualize(G, pos)
