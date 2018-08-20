import sys
import networkx as nx
from plot import *
from simulate import *
from numpy import vstack, zeros
import numpy as np

# Global Constants
NEUTRAL = 2
PASSIVE = 1
EXTREMIST = 0

# Global Population variables
n = 50 # population
seed = 42 # for random processes
initPE = .01 # percent of population that initallally has extreme views
density = .2 # number of groups relative to size of population
passiveProb = .2 # probability a general population node is disosed to be passive
maxExtremistOutDegree = 3 # maximum number of out connections from extremists to general population


def initGeneralPopulation():
    # General Population variables
    gpEdgeProb = .5 # Probability for edge creation
    gpN = int (n * (1-initPE)) # general population inital number
    gpGroups = int (density * gpN) +1
    gpGroupSize = int (1 / density)
    gpEdgeWeight = 1

    # create graph
    gp = nx.relaxed_caveman_graph(gpGroups, gpGroupSize, gpEdgeProb, seed=seed)

    # label all depending on probability of passive or not
    for u,d in list(gp.nodes(data=True)):
        d['type'] = PASSIVE if (np.random.uniform(0,1, 1) < passiveProb) else NEUTRAL

    # reweight the edges
    for (u, v) in gp.edges:
        gp[u][v]['weight'] = gpEdgeWeight

    # return the new graph
    return gp

def initExtremePopulation():
    # Extremist Population variables
    epN = int(n *initPE) # extreme population inital number
    epEdgeProb = .7 # probabilty of rewiring edges
    epGroups = int (density * epN) + 1
    epGroupSize = int (1 / density)
    epEdgeWeight = 1

    #create the new graph
    ep = nx.relaxed_caveman_graph(epGroups, epGroupSize, epEdgeProb, seed=seed)

    # reweight the edges
    for (u, v) in ep.edges:
        ep[u][v]['weight'] = epEdgeWeight

    # label all as extremists
    for u,d in list(ep.nodes(data=True)):
        d['type'] = EXTREMIST

    #return the new graph
    return ep

def mergePopulations(generalGraph, extremistGraph, censorProbWeight):
    # combine populations
    p = nx.disjoint_union(extremistGraph, generalGraph)

    # create connections between the two disparate graphs
    for node in p.nodes():
        # if extremist add connections to general population
        if (p.nodes[node]['type'] == EXTREMIST):
            # pick random number for extremist out degree
            for i in range(np.random.randint(0,maxExtremistOutDegree)):
                #pick random node, create connection from the general population
                connection  = np.random.randint(len(extremistGraph),len(generalGraph) + len(extremistGraph))
                p.add_edge(node,connection,weight=censorProbWeight)

    return p

def initializeFitness(population):
    for node,d in list(population.nodes(data=True)):
        d['fitness'] = calculateFitness(population, node)

def initializePopulation(censorProbWeight):
    # create population graphs and store nodes
    gGraph = initGeneralPopulation()
    eGraph = initExtremePopulation()

    # merge the populations
    p = mergePopulations(gGraph, eGraph, censorProbWeight)

    # initialize the fitness for the nodes in the population
    initializeFitness(p)

    return p
