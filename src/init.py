import sys
import networkx as nx
from plot import *
from numpy import vstack, zeros
import numpy as np
import random

# Global Constants
NEUTRAL = 0
PASSIVE = 1
EXTREMIST = 2

# Global Population variables
n = 100 # population
seed = 42 # for random processes
initPE = .02 # percent of population that initallally has extreme views
density = .2 # number of groups relative to size of population
censorProb = .3 # w
passiveProb = .3 # probability a general population node is disosed to be passive

def initGeneralPopulation():
    # General Population variables
    gpEdgeProb = .3 # Probability for edge creation
    gpN = int (n * (1-initPE)) # general population inital number
    gpGroups = int (density * gpN) +2
    gpGroupSize = int (1 / density)
    gpEdgeWeight = 1

    # create graph
    gp = nx.relaxed_caveman_graph(gpGroups, gpGroupSize, gpEdgeProb, seed=seed)

    # label all as extremists
    for u,d in list(gp.nodes(data=True)):
        d['type'] = EXTREMIST

    # reweight the edges
    for (u, v) in gp.edges:
        gp[u][v]['weight'] = gpEdgeWeight

    # return the new graph
    return gp

def initExtremePopulation():
    # Extremist Population variables
    epN = int(n *initPE) # extreme population inital number
    epEdgeProb = .7 # probabilty of rewiring edges
    epGroups = int (density * epN) +2
    epGroupSize = int (1 / density)
    epEdgeWeight = 1

    #create the new graph
    ep = nx.relaxed_caveman_graph(epGroups, epGroupSize, epEdgeProb, seed=seed)

    # label all as extremists
    for u,d in list(ep.nodes(data=True)):
        d['type'] = PASSIVE if (random.uniform(0, 1) < passiveProb) else NEUTRAL

    # reweight the edges
    for (u, v) in ep.edges:
        ep[u][v]['weight'] = epEdgeWeight

    #return the new graph
    return ep

def initializePopulation():
    # create population graphs and store nodes
    gGraph = initGeneralPopulation()
    print(len(gGraph))
    eGraph = initExtremePopulation()
    print(len(eGraph))

    # combine populations
    p = nx.compose(eGraph,gGraph)

    for u,v in p.edges():
        if (p.nodes[u]['type'] == EXTREMIST):
            p[u][v]['weight'] = censorProb

    return p
