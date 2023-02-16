file = "day8/day8-input.txt"

forest = []
visibleTrees = 0

with open(file) as f:
    x = len(f.readline()) - 1
    for i in range(x):
        forest.append([])

    #print(forest)

with open(file) as f:
    for line in f:
        #print(line)
        for i in range(x):
            forest[i].append(line[i])

y = len(forest[0])
scenicScores = []

c = 1 #start at column one to avoid the edges
while c < x:
    r = 1

    while r < y:
        scenicScore = 1
        current = forest[c][r]

        #look right
        numRVis = 0
        lr = c - 1
        while lr >= 0:
            numRVis += 1

            if forest[lr][r] >= current:
                break

            lr -= 1

        #look left
        numLVis = 0
        ll = c + 1
        while ll < x:
            numLVis += 1

            if forest[ll][r] >= current:
                break

            ll += 1

        #look up
        numAVis = 0
        la = r - 1
        while la >= 0:
            numAVis += 1
            
            if forest[c][la] >= current:
                break

            la -= 1

        #look below
        numBVis = 0
        lb = r + 1
        while lb < y:
            numBVis += 1

            if forest[c][lb] >= current:
                break

            lb += 1

        scenicScore = numAVis * numBVis * numLVis * numRVis
        scenicScores.append(scenicScore)

        r += 1

    c += 1

highest = 0

for i in range (len(scenicScores) - 1):
    if scenicScores[i] > highest:
        highest = scenicScores[i]

print(highest)