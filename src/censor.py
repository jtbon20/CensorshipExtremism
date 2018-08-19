import sys
import networkx as nx
from plot import *
from init import *
from simulate import *
from numpy import vstack, zeros
import numpy as np

#Arguments
if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

# Program Constants
filename = sys.argv[1]

# Simulation Constants
censorProbWeight = 1 # w
simulationTime = 1000

#initialize simulation
G = initializePopulation(censorProbWeight)

plt.ion()

#run the simulation
runSimulation(G, simulationTime)
