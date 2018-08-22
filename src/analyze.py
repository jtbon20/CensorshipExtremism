# Global Constants
NEUTRAL = 2
PASSIVE = 1
EXTREMIST = 0

def avgFitnessByPopulation(G):
    ePop = 1
    pPop = 1
    nPop = 1
    eTotal = 0
    pTotal = 0
    nTotal = 0

    for u,d in list(G.nodes(data=True)):
        type = d['type']

        if (type == NEUTRAL):
            nPop += 1
            nTotal += d['fitness']
        elif (type == PASSIVE):
            pPop += 1
            pTotal += d['fitness']
        else:
            ePop += 1
            eTotal += d['fitness']

    print(round(nTotal/nPop, 2),nPop,round(pTotal/pPop,2),pPop,round(eTotal/ePop,2),ePop)

def scoreFinalPopulation(G):
    ePop = 0
    pPop = 0
    nPop = 0

    for u,d in list(G.nodes(data=True)):
        type = d['type']

        if (type == NEUTRAL): nPop += 1
        elif (type == PASSIVE): pPop += 1
        else: ePop += 1

    return (1*ePop + 0 * pPop + 0 * nPop) / (ePop + pPop + nPop)
