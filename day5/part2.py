##to parse the txt file
#   each stack is a different list
#   
#   stop parsing lists after the one line of consecuative numbers and a empty line
file = "day5/day5-input.txt"

numCrates = 0
l = []
l2 = []

with open(file) as f:
    ##parsing the crates -_-
    for line in f: #finding number of crates
        if line.strip()[:1].isnumeric():
            numCrates = line.strip()[len(line.strip()) - 1]
    
    numCrates = int(numCrates)

for i in range(numCrates):
        l.append([i])
        l2.append([i])
#print(list)

with open(file) as f:
    for line in f:
        if line.strip()[:1].isnumeric():
            break

        for i in range(numCrates):
            l[i].append(line[(4*i + 1):(4*i +2)])
           

for i in range(numCrates):
    l[i].pop(0)
    l[i].reverse()


for i in range(numCrates):
    kLen = len(l[i])

    for k in range(kLen):
        if l[i][k] != ' ':
            l2[i].append(l[i][k])

for i in range(numCrates):
    l2[i].pop(0)



#for the moving stuff around
with open(file) as f:
    for line in f:
        if line.startswith('m'):
            instructions = line.strip().partition("from") 
            stacks = instructions[2].strip().split("to")

            amt = int(instructions[0].strip().split(" ")[1])

            origIndex = int(stacks[0].strip()) - 1
            newIndex = int(stacks[1].strip()) - 1

            if amt == 1:
                lastEltIndex = len(l2[origIndex]) - 1
                elt = l2[origIndex][lastEltIndex]

                l2[origIndex].pop(lastEltIndex)
                l2[newIndex].append(elt)

            else:
                llen = len(l2[origIndex])

                for i in range(amt):
                    ind = llen - amt + i #amt - i - 1

                    elt = l2[origIndex][ind]
                    l2[newIndex].append(elt)
                
                for i in range(amt):
                    ind = llen - i - 1
                
                    l2[origIndex].pop(ind)

#print(l2)

finalL = []

for i in range(numCrates):
    finalL.append(l2[i][len(l2[i]) - 1])

print(finalL)
    
            