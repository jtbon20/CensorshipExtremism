import sys
import networkx as nx
from init import *
from simulate import *
import numpy as np

#Arguments
if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

# Program Constants
filename = sys.argv[1]

# Simulation Constants
censorProbWeight = .1 # w
inComCensorWeight = censorProbWeight # q
simulationTime = 1000

#initialize simulation
G = initializePopulation(filename, censorProbWeight)

#run the simulation
runSimulation(G, simulationTime, inComCensorWeight)
