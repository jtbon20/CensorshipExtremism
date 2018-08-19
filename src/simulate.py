import sys
import networkx as nx
from plot import *
from numpy import vstack, zeros
import numpy as np

# Global Constants
NEUTRAL = 0
PASSIVE = 1
EXTREMIST = 2

# values for the payoff matrix
a = .3 # benefit from E > E (agreementCoef)
b = .5 # gain from converting N>E (conversionCoef)
c = 1 # cost of revealing views to non-believer  (badRevealCoef )
d = .01 # delta (conversationCoef)

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
            neighborFitness[v] = calculateFitness(G, v)

        # get total fitness
        totalFit = sum(neighborFitness.values())

        # normalize and return
        return {k: v / totalFit for k, v in neighborFitness.items()}
    else:
        return {}
# return a strategy based on probabilities
def getStrategy(G, stratProbs):
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

def updateFitness(G, node, strategy):
    # loop over, calculate and add into dict
    for u,v in G.edges(node):
        G.nodes[node]['fitness'] = calculateFitness(G, v)

def runSimulation(G, max):
    # run simulation, for i time clicks
    i = 0

    while (i < max):
        #pick random node inside the graph
        node = np.random.randint(0,len(G)-1)

        # get the normalized fitness to pick the probabilistic strategy
        neighborFitness = getNormalizedFitness(G, node)

        # based on the probabilities, get a new strategy
        newStrategy = getStrategy(G, neighborFitness)
        G.nodes[node]['type'] = newStrategy

        # if need to update strategy
        if (newStrategy != G.nodes[node]['type']):
            updateFitness(G, node, newStrategy)

        #plot result
        visualize(G, 'tmp')

        #increment count
        i += 1
