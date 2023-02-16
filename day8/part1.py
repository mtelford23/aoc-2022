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
    
    #print(forest)
    
y = len(forest[0]) #- 1
visableTrees = 2* (len(forest[0]) + len(forest)) - 4

for i in range(x-1):
    if i == 0: 
        continue

    elif i == x - 1:
        break

    else:
        for k in range(y-1):
            if k == 0 or k == y:
                continue

            current = forest[i][k]
            visableL = True
            visableR = True
            visableB = True
            visableA = True

            #look to left of current
            for q in range(k):
                comp = forest[i][q]
                if comp >= current:
                    visableL = False
                    break

            #look to right of current
            for q in range (x - k): 
                if q + k == k:
                    continue

                comp = forest[i][q + k]
                if comp >= current:
                    visableR = False
                    break
            
            #look above current
            for q in range(i): 
                comp = forest[q][k]
                if comp >= current:
                    visableA = False
                    break

            #look below current
            for q in range(y - i): 
                if q + i == i:
                    continue

                comp = forest[q + i][k]
                if comp >= current:
                    visableB = False
                    break
            

            if visableA or visableB or visableL or visableR:
                #print(i, current)
                visableTrees += 1

print(visableTrees)

