import networkx as nx
from plot import *
from simulate import *
import numpy as np

# Global Constants
NEUTRAL = 2
PASSIVE = 1
EXTREMIST = 0

# Global Population variables
g = 50 # groups in general population
gs = 4 # group size in populations
seed = 42 # for random processes
initPE = .05 # percent of population that initallally has extreme views
passiveProb = .2 # probability a general population node is disosed to be passive
maxExtremistOutDegree = 4 # maximum number of out connections from extremists to general population


def initGeneralPopulation():
    # General Population variables
    gpEdgeProb = .6 # Probability for edge creation
    gpEdgeWeight = 1

    # create graph
    gp = nx.relaxed_caveman_graph(g, gs, gpEdgeProb, seed=seed)

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
    epEdgeProb = .9 # Probability for edge creation
    epEdgeWeight = 1
    epGroups = int(initPE * g) + 1

    #create the new graph
    ep = nx.relaxed_caveman_graph(epGroups, gs, epEdgeProb, seed=seed)

    # reweight the edges
    for (u, v) in ep.edges:
        ep[u][v]['weight'] = epEdgeWeight

    # label all as extremists
    for u,d in list(ep.nodes(data=True)):
        d['type'] = EXTREMIST

    #return the new graph
    return ep

def mergePopulations(generalGraph, extremistGraph):
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
                p.add_edge(node,connection,weight=.1)

    return p

def initializePopulation():
    # create population graphs and store nodes
    gGraph = initGeneralPopulation()
    eGraph = initExtremePopulation()

    # merge the populations
    p = mergePopulations(gGraph, eGraph)

    return p
