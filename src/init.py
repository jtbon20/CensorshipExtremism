import sys
import networkx as nx
from plot import *
from numpy import vstack, zeros
import numpy as np


# Global Population variables
n = 100 # population
seed = 42 # for random processes
initPE = .02 # percent of population that initallally has extreme views
density = .2 # number of groups relative to size of population

def initGeneralPopulation():
    # General Population variables
    gpEdgeProb = .3 # Probability for edge creation
    gpN = int (n * (1-initPE)) # general population inital number
    gpGroups = int (density * gpN) +2
    gpGroupSize = int (1 / density)

    # return the new graph
    return nx.relaxed_caveman_graph(gpGroups, gpGroupSize, gpEdgeProb, seed=seed)

def initExtremePopulation():
    # Extremist Population variables
    epN = int(n *initPE) # extreme population inital number
    epEdgeProb = .7 # probabilty of rewiring edges
    epGroups = int (density * epN) +2
    epGroupSize = int (1 / density)

    #return the new graph
    return nx.relaxed_caveman_graph(epGroups, epGroupSize, epEdgeProb, seed=seed)
